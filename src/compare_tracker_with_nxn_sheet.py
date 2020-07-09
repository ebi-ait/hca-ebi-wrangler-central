"""
Little script that compares the HCA dataset tracking sheet
(https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0) with Valentine
Svensson's curated single cell database (http://www.nxn.se/single-cell-studies)

The output is a formatted list that can be copied over to the dataset tracking sheet.

Usage: python3 compare_tracker_with_nxn_sheet.py
"""

import requests as rq

def select_unique_studies(valentines_sheet, tracking_sheet):
    valentine_dois = set([data[1] for data in valentines_sheet])

    tracking_sheet_dois = set([track[13] for track in tracking_sheet if track[13]])
    # Little data massage
    tracking_sheet_dois = {f"10.{doi.split('doi.org/10.')[-1]}" for doi in tracking_sheet_dois if "doi.org" in doi}

    unregistered_dois = valentine_dois - tracking_sheet_dois

    unregistered_table = [row for row in valentines_sheet if row[1] in unregistered_dois]

    valentine_accessions = set([data[11] for data in unregistered_table if data[11]])
    tracking_sheet_accessions = set([track[1] for track in tracking_sheet if track[1]])

    unregistered_accessions = valentine_accessions - tracking_sheet_accessions

    second_unregistered_table = [row for row in unregistered_table if row[11] in unregistered_accessions]

    valentine_titles = set([data[4].lower() for data in second_unregistered_table if data[4]])
    tracking_sheet_titles = set([track[14].lower() for track in tracking_sheet if track[14]])

    unregistered_titles = valentine_titles - tracking_sheet_titles

    full_unregistered_table = [row for row in second_unregistered_table if row[4].lower() in unregistered_titles]

    return full_unregistered_table


def filter_table(valentines_table):
    filtered_table = [row for row in valentines_table if row[8].lower() in ['human', 'human, mouse', 'mouse, human']]
    filtered_table = [row for row in filtered_table if
                    row[10].lower() in ["chromium", "drop-seq", "dronc-seq", "smart-seq2", "smarter", "smarter (C1)"]]
    filtered_table = [row for row in filtered_table if row[13].lower() == 'rna-seq']
    return filtered_table


def print_output(filtered_table):
    table_final = []
    for row in filtered_table:
        table_final.append(
            [f"https://doi.org/{row[1]}", row[4], row[7], row[8], row[9], row[10], row[15], row[11], f"{row[14]} {row[16]}"])

    tabu = '\t'
    for r in table_final:
        print(tabu + r[7] + tabu * 12 + r[0] + tabu + r[1] + tabu * 5 + r[4] + tabu * 10 + r[3] + tabu + r[5] + tabu * 3 + r[
            6] + tabu * 2 + r[2] + tabu * 4 + r[-1])


def main():
    valentines_database = rq.get('http://www.nxn.se/single-cell-studies/data.tsv', headers={'Cache-Control': 'no-cache'})
    valentines_database.encoding = 'utf-8'
    valentines_database = valentines_database.text.splitlines()
    valentines_database = [data.split("\t") for data in valentines_database][1:]

    tracking_sheet = rq.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ26K0ZYREykq2kR2HgA3xGol3PfFuwYuqNBQCZgi4L7yqF2GZiNdXfQ19FtjxMvCk8IU6S_v6zih9z/pub?gid=0&single=true&output=tsv", headers={'Cache-Control': 'no-cache'}).text.splitlines()
    tracking_sheet = [data.split("\t") for data in tracking_sheet][1:]

    entries_not_registered = select_unique_studies(valentines_database, tracking_sheet)
    filtered_table = filter_table(entries_not_registered)

    print_output(filtered_table)


if __name__ == '__main__':
    main()
