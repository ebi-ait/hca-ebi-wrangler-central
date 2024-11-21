import requests
import argparse
import boto3
import json
from werkzeug.datastructures import FileStorage


def parse_arguments(parser: argparse.ArgumentParser) -> argparse.Namespace:
    parser.add_argument('-u', '--upload-area', help='HCA-Util upload area UUID', required=True)
    parser.add_argument('-s', '--spreadsheet-name', help='Name of the spreadsheet in the HCA-util area', required=True)
    parser.add_argument('-t', '--token', help='JWT token to authorize submission creation', required=True)
    parser.add_argument('-p', '--project-uuid', help='Project UUID to attach the submission to', required=True)
    parser.add_argument('-e', '--environment', help='Ingest environment. Defaults to staging.', choices=['dev', 'staging', 'prod'], default='staging', required=False)
    parser.add_argument('-d', '--update-project', help='Wether to update project with spreadsheet', action='store_true', default=False, required=False)
    args = parser.parse_args()
    return args


def base_url(environment):
    environment = f'{environment}.' if environment != 'prod' else ''
    return f"https://ingest.{environment}archive.data.humancellatlas.org"

def main(upload_area_uuid, spreadsheet_name, token, environment, project_uuid, update_project):
    s3 = boto3.session.Session().resource('s3')
    s3_obj = s3.Object(bucket_name='hca-util-upload-area', key=f'{upload_area_uuid}/{spreadsheet_name}')
    headers = {'Authorization': f'Bearer {token}'}
    url = f'{base_url(environment)}/api_upload'
    params = json.dumps({'projectUuid': project_uuid,
                         'isUpdate': False,
                         'updateProject': update_project})
    full_object = s3_obj.get()
    spreadsheet = FileStorage(stream=full_object['Body'], filename=spreadsheet_name, name=spreadsheet_name,
                              content_type=full_object['ContentType'], content_length=full_object['ContentLength'])
    r = requests.post(url=url, data={'params': params}, files={'file': spreadsheet}, headers=headers)
    r.raise_for_status()
    print(r.json())
    return r

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parse_arguments(parser)
    main(args.upload_area, args.spreadsheet_name, args.token, args.environment, args.project_uuid, args.update_project)
