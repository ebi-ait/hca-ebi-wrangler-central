import requests as rq
import re
import ftplib
import argparse
from io import BytesIO
import gzip
import os
import tarfile
from inspect import getmembers, isfunction
import shutil

from tqdm import tqdm

import reader_functions_cell_counter

class NoMatrixFolder(Exception):
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-g', '--geo-accession', help="Geo accession")
    parser.add_argument('-r', '--reader-function', help='Reader function to be called', default='tenx_mex_format')
    parser.add_argument('-d', '--download-mode', action='store_true', help='Only download matrices and decompress', default=False)
    args = parser.parse_args()
    return args

def get_series_matrix_path(connection: ftplib.FTP):
    dirlist = []
    connection.retrlines('LIST', dirlist.append)
    if not any(['matrix' in line for line in dirlist]):
        raise NoMatrixFolder("Matrix folder not found")
    connection.cwd('matrix')
    series_matrix_txt = connection.nlst()[0]
    bio = BytesIO()
    connection.retrbinary(f"RETR {series_matrix_txt}", callback=bio.write)
    bio.seek(0) # Go back to the start
    zippy = gzip.GzipFile(fileobj=bio)
    uncompressed = zippy.read().decode('utf-8').splitlines()
    series_supplementary_file = [row for row in uncompressed if row.startswith('!Series_supplementary_file')][0]
    return re.search("ftp://.*?\\.tar", series_supplementary_file).group()


def download_tar_file(path):
    filename = path.split('/')[-1]
    print(f"Downloading tar file to {filename}")
    with rq.get(path, stream=True) as r:
        r.raise_for_status()
        total_size_in_bytes= int(r.headers.get('content-length', 0))
        block_size = 1024 * 1024
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(filename, 'wb') as f:
            for data in r.iter_content(chunk_size=block_size):
                progress_bar.update(len(data))
                f.write(data)
    return filename


def decompress_tar_file(tar_file, output_path):
    tar = tarfile.open(tar_file)
    tar.extractall(output_path)


def decompress_all_gzip_files(path):
    files = os.listdir(path)
    for f in files:
        with gzip.open(path + f, 'rb') as f_in:
            with open(path + f.replace('.gz', ''), 'w') as f_out:
                f_out.write(f_in.read().decode())


def remove_gz_files(path):
    files = [f for f in os.listdir(path) if f.endswith('gz')]
    [os.remove(f"{path}{f}") for f in files]


def get_reader_functions():
    return {a[0]: a[1] for a in getmembers(reader_functions_cell_counter) if isfunction(a[1])}

def select_reader_function(reader_functions):
    print("Please select:")
    function_names = list(reader_functions.keys())
    for i, function_name in enumerate(function_names):
        print(f"\t{i}-{function_name}")
    function_number = int(input())
    return reader_functions[function_names[function_number]]


def clean(series_matrix_path):
    shutil.rmtree('Matrices/')
    os.remove(series_matrix_path)

def main(geo_accession, reader_function, download_mode=False):
    connection = ftplib.FTP(f'ftp.ncbi.nlm.nih.gov')
    connection.login()
    connection.cwd(f'geo/series/{geo_accession[:-3] + "nnn"}/{geo_accession}/')
    try:
        series_matrix_path = get_series_matrix_path(connection)
        print(series_matrix_path)
    except Exception as e:
        print(e)
    finally:
        connection.close()
    if not os.path.exists(series_matrix_path.split('/')[-1]):
        download_tar_file(path=series_matrix_path.replace('ftp://', 'https://'))
        print("Files downloaded.")
    try:
        os.makedirs('Matrices')
    except Exception as e:
        print("Output folder already exists")
    decompress_tar_file(series_matrix_path.split('/')[-1], 'Matrices/')
    decompress_all_gzip_files('Matrices/')
    remove_gz_files('Matrices/')
    if not download_mode:
        reader_functions = get_reader_functions()
        if not reader_function or not reader_function in reader_functions:
            to_call = select_reader_function(reader_functions)
        else:
            to_call = reader_functions[reader_function]

        cell_count = to_call('Matrices/')
        print(cell_count)
        clean(series_matrix_path.split('/')[-1])


if __name__ == '__main__':
    args = parse_args()
    main(args.geo_accession, args.reader_function, args.download_mode)