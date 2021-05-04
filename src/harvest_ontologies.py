#!/usr/bin/env python3

import requests as rq
import argparse
import pandas
from ingest.template.schema_template import SchemaTemplate


def define_parser():
    parser = argparse.ArgumentParser(description="Parser for the arguments")
    parser.add_argument("--spreadsheet", "-s", action="store", dest="wb_name", type=str, help="Input spreadsheet name")
    return parser