
from ingest.api.ingestapi import IngestApi
import requests as rq
import re
import argparse
import sys
import json
import base64

def define_parser():
    parser = argparse.ArgumentParser(description="Parser for the arguments")
    parser.add_argument("--environment", "-e", action="store", dest="env", type=str,
                        help="environment you want to submit to", default="prod")
    parser.add_argument("--token", "-t", action="store", dest="token", type=str,
                        help="token to give permission to submit to ingest env specified")
    parser.add_argument("--doi", "-d", action="store", dest="doi", type=str,
                        help="doi of the publication")
    return parser


def get_pub_info(article_doi):
    try:
        europmc_api = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=doi:"
        headers = {"Accept": "application/json"}
        request_url = europmc_api + article_doi + "&resultType=core&cursorMark=*&pageSize=25&format=json"
        print("searching EuroPMC using this url: {}".format(request_url))
        response = rq.get(request_url, headers=headers)
        result = response.json()['resultList']['result'][0]
        print("Publication with title '{}' found in EuroPMC".format(result['title']))
        return result
    except IndexError:
        print("doi not found, check doi")
        sys.exit(0)
    except KeyError:
        print("doi not found, check doi")
        sys.exit(0)


def construct_project_json(publication_info, project_schema_url):
    try:
        project_core = {"project_short_name": "tba",
                        "project_title": publication_info['title']}
        if 'abstractText' in publication_info.keys():
            project_core["project_description"] = publication_info['abstractText']
        contributors = []
        for author in publication_info['authorList']['author']:
            this_contributor = {}
            if 'firstName' in author.keys():
                this_contributor["name"] = author['firstName'].replace(" ", ",") + "," + author['lastName']
                if 'authorAffiliationDetailsList' in author.keys():
                    this_contributor['laboratory'] = ''
                    email_regex = re.compile('[\w\.-]+@[\w\.-]+\.\w+')
                    # Extract email address and set as corresponding if email in string
                    if re.search(email_regex, author['authorAffiliationDetailsList']['authorAffiliation'][0]['affiliation']):
                        this_contributor['corresponding_contributor'] = True
                        this_contributor['email'] = re.search(email_regex,
                                                              author['authorAffiliationDetailsList']['authorAffiliation'][0]
                                                              ['affiliation']).group()
                    ror_affiliation_api_url = "https://api.ror.org/organizations?affiliation="
                    affiliation_response = rq.get(ror_affiliation_api_url + author['authorAffiliationDetailsList']['authorAffiliation'][0]['affiliation']).json()
                    highest_match = affiliation_response['items'].pop(0)
                    if highest_match['score'] == 1.0:
                        this_contributor['institution'] = highest_match['organization']['name']
                        this_contributor['country'] = highest_match['organization']['country']['country_name']
                    for item in affiliation_response['items']:
                        if item['score'] == 1.0 and this_contributor['institution'] is not item['organization']['name']:
                            this_contributor['laboratory'] = this_contributor['laboratory'] + ' ' + item['organization']['name']
                        else:
                            break
                    if this_contributor['laboratory'] == '' or not 'institution' in this_contributor.keys():
                        this_contributor['laboratory'] = author['authorAffiliationDetailsList']['authorAffiliation'][0]['affiliation']

                    # Extract country from string if org not found in ror
                    if 'country' not in this_contributor.keys():
                        split_lab = re.split("[, .:]", this_contributor["laboratory"])
                        split_lab.reverse()
                        for part in split_lab:
                            if rq.get("https://restcountries.eu/rest/v2/name/{}?fullText=true".format(part)):
                                this_contributor["country"] = part
                                break

            elif 'collectiveName' in author.keys():
                this_contributor['name'] = author['collectiveName']
                this_contributor['institution'] = 'not applicable'

            if "authorId" in author.keys():
                if author["authorId"]["type"] == "ORCID":
                    this_contributor["orcid_id"] = author["authorId"]["value"]
            contributors.append(this_contributor)

        # set publication info
        publications = []
        publication = {
            "authors": publication_info['authorString'].split(", "),
            "title": publication_info['title'],
            "doi": publication_info['doi'],
            "pmid": int(publication_info['pmid']) if 'pmid' in publication_info.keys() else None,
            "url": "https://doi.org/" + publication_info['doi']
        }
        publications.append(publication)

        # get grant info
        if 'grantsList' in publication_info.keys():
            funders = []
            for grant in publication_info['grantsList']['grant']:
                this_funder = {"grant_id": grant['grantId'],
                               "organization": grant['agency']}
                funders.append(this_funder)



        content = {
            "project_core": project_core,
            "contributors": contributors,
            "publications": publications,
            "funders": funders,
            "schema_type": "project",
            "describedBy": project_schema_url
        }

        project_dict = {"releaseDate": "2021-01-04T00:00:00.000Z",
                        "content": content}

        return project_dict
    except KeyError as e:
        print("Could not parse publication info properly")
        print(e)
        sys.exit()


def main(environment, auth_token, doi):
    pub_info = get_pub_info(doi)

    if environment == "prod":
        env = ""
    elif environment == "staging":
        env = "staging."
    else:
        env = "dev."
    ingest_api_url = "http://api.ingest.{}archive.data.humancellatlas.org".format(env)
    ingest_api = IngestApi(ingest_api_url)
    latest_project_schema = ingest_api.get_schemas(high_level_entity="type",
                                                   domain_entity="project",
                                                   concrete_entity="project")[0]['_links']['json-schema']['href']
    project_json = construct_project_json(pub_info, latest_project_schema)
    submission_headers = {'Authorization': 'Bearer {}'.format(auth_token),
                          'Content-Type': 'application/json'}

    response = rq.post("{}/projects".format(ingest_api_url),
                       data=json.dumps(project_json),
                       headers=submission_headers)
    if response:
        print("Project with uuid '{}' successfully created in {}.".format(
            response.json()['uuid']['uuid'], environment))
        print("View the created project here: https://{}contribute.data.humancellatlas.org/projects/detail?uuid={}".format(env, response.json()['uuid']['uuid']
        ))
        with open("log.txt", "a") as log_file:
            log_file.write(doi + "\t" + response.json()['uuid']['uuid'] + "\n")
    else:
        print("No project created, check if your token is still valid.")


if __name__ == "__main__":
    parser = define_parser()
    args = parser.parse_args()
    main(args.env,
         args.token,
         args.doi)
