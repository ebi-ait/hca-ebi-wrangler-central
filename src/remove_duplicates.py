# coding=utf-8
"""
Little script that identifies duplicates in the dataset tracking sheet
(https://docs.google.com/spreadsheets/d/1rm5NZQjE-9rZ2YmK_HwjW-LgvFTTLs7Q6MzHbhPftRE/edit#gid=0)
The output is a tab delimited .txt file consisting of the duplicate entries. This can be used to manually remove
duplicate entries from the tracker sheet.
Usage: python3 remove_duplicates.py
Last time updated:
2020-12-14T10:08:46.801271Z
"""

import os
import re
import requests as rq
import Levenshtein
from Levenshtein import *
import pandas as pd
import itertools
from datetime import datetime


class ChangedHeaders(Exception):
    def __init__(self, header):
        super().__init__(f"Headers changed, couldn't find {header}")

def reformat_title(title: str):
    characters_to_remove = [" ",".",",","-","_",":"]
    for character in characters_to_remove:
        title = title.replace(character,'').lower().strip()
    return title

def get_distance_metric(title1: str,title2: str):
    if title1 == '' or title2 == '':
        return None
    else:
        max_len = max(len(title1),len(title2))
        dist_metric = 100-(Levenshtein.distance(title1, title2)/max_len)*100
        return dist_metric

def find_duplicates(tracking_sheet: pd.DataFrame):
    """
    Find duplicates in tracker sheet based on:
        - DOI (doi; pub_link): exact match to the doi; exact match to a doi within a link
        - Accession(s) (data_accession): exact match to a string in a list of accession(s)
        - Publication title (pub_title): approximate match (distance metric)
        - Publication link (pub_link): exact match to the full publication link
        - pmid: exact match to the pmid

    :param tracking_sheet: pd.DataFrame
                           DataFrame representing the Dataset Tracking Sheet
    :return:
    """
    indices = []
    length = tracking_sheet.shape[0]

    for i, j in itertools.combinations(range(length), 2):
        if list(tracking_sheet['pmid'])[i].strip() in list(tracking_sheet['pmid'])[j].strip() and list(tracking_sheet['pmid'])[i].strip() != '':
            indices.append(i)

    for i, j in itertools.combinations(range(length), 2):
        if list(tracking_sheet['doi'])[i].strip() in list(tracking_sheet['doi'])[j].strip() and list(tracking_sheet['doi'])[i].strip() != '' and list(tracking_sheet['doi'])[i].strip() != '10.1038/NA':
            indices.append(i)

    for i, j in itertools.combinations(range(length), 2):
        if list(tracking_sheet['doi'])[i].strip() in list(tracking_sheet['pub_link'])[j].strip() and list(tracking_sheet['doi'])[i].strip() != '':
            indices.append(i)

    # Look for exact matches within the list of accessions
    for i, j in itertools.combinations(range(length), 2):
        accession1 = list(tracking_sheet['data_accession'])[i]
        accession2 = list(tracking_sheet['data_accession'])[j]
        if ',' not in accession1 and ';' not in accession1:
            if accession1.strip() in accession2 and accession1.strip() != '':
                indices.append(i)
        else:
            if ',' in accession1:
                accessions = accession1.split(',')
            elif ';' in accession1:
                accessions = accession1.split(';')
            else:
                accessions = accession1
            for accession in accessions:
                if accession in accession2:
                    indices.append(i)

    # look for approximate matches to the publication title
    tracking_sheet['reformatted_pub_title'] = [reformat_title(i) for i in tracking_sheet['pub_title']]
    for i, j in itertools.combinations(range(length), 2):
        if list(tracking_sheet['reformatted_pub_title'])[i] != '' and list(tracking_sheet['reformatted_pub_title'])[i] != 'unspecified':
            dist_metric = get_distance_metric(list(tracking_sheet['reformatted_pub_title'])[i],list(tracking_sheet['reformatted_pub_title'])[j])
            if dist_metric is None:
                continue
            else:
                if dist_metric >= 97:
                    indices.append(i)

    indices = list(set(indices))
    if indices is not None:
        duplicate_entries = tracking_sheet.iloc[indices]
        return duplicate_entries
    else:
        None

def update_timestamp():
    script_path = os.path.realpath(__file__)
    with open(script_path, 'r') as f:
        script = f.read()

    timestamp = datetime.now()
    timestamp_str = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    script = re.sub('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}Z', timestamp_str, script, count=1)

    with open(script_path, 'w') as f:
        f.write(script)

def main():

    # Get tracking sheet and transform it into a matrix
    tracking_sheet = rq.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ26K0ZYREykq2kR2HgA3xGol3PfFuwYu"
                            "qNBQCZgi4L7yqF2GZiNdXfQ19FtjxMvCk8IU6S_v6zih9z/pub?gid=0&single=true&output=tsv",
                            headers={'Cache-Control': 'no-cache'}).text.splitlines()
    tracking_sheet = [data.split("\t") for data in tracking_sheet]
    cols = tracking_sheet[0]
    tracking_sheet = tracking_sheet[1:]
    tracking_sheet = pd.DataFrame(tracking_sheet, columns=cols)

    # Compare and filter
    duplicate_entries = find_duplicates(tracking_sheet)
    if duplicate_entries is None:
        print("No duplicate entries found")
    else:
        duplicate_entries = duplicate_entries[['data_accession','pub_title','reformatted_pub_title','pub_link','pmid','doi']]
        duplicate_entries.to_csv("duplicate_entries.txt",sep="\t")

    update_timestamp()

if __name__ == '__main__':
    main()
