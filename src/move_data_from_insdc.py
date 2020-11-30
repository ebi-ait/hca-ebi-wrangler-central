import boto3
from botocore.exceptions import ClientError
import os
from tqdm import tqdm
from smart_open import open as op
import requests as rq
import argparse
import xmltodict
from urllib.request import urlopen
from urllib.request import OpenerDirector
from urllib.parse import quote_plus
from urllib.parse import unquote_plus
from multiprocessing import Pool
from io import BytesIO
from xml.parsers.expat import ExpatError
from time import sleep
from collections import OrderedDict


def parse_args() -> argparse.Namespace:
    """
    Create the parser and parse the arguments.

    :returns parser: argparse.ArgumentParser()
                     Argument parser
    """
    # parse command-line arguments

    parser = argparse.ArgumentParser()
    parser.add_argument('--study_accession', "-s", type=str,
                        help='Study accession in ENA')
    parser.add_argument('--output_path', "-o", default='.',
                        help='path where files will be downloaded: can be local or s3')
    parser.add_argument('--threads', "-t", default=1, type=int,
                        help='Number of processes to simultaneously spam')
    parser.add_argument('--allowed', "-a", type=str,
                       help='Full path to plain text file with line separated list of files that should be transferred.')

    return parser.parse_args()

def retrieve_from_ae(study_accession: str) -> list:
    request_url = (f"https://www.ebi.ac.uk/arrayexpress/json/v3/experiments/{study_accession}/files")
    request = rq.get(request_url)
    file_list_dicts = request.json()['files']['experiment']['file']
    files = [x['url'] for x in file_list_dicts]
    not_available = None
    return files, not_available


def retrieve_from_ena(study_accession: str) -> list:
    field = "submitted_ftp" if "PRJEB" in study_accession else "fastq_ftp"
    request_url = (f"https://www.ebi.ac.uk/ena/data/warehouse/filereport?accession={study_accession}"
                   f"&result=read_run&fields={field}")
    request = rq.get(request_url)
    lines = request.text.splitlines()[1:]
    not_available = [line.split('\t')[0] for line in lines if not line.split('\t')[1]]
    lines = [line.split('\t')[1] for line in lines]
    files = []
    [files.extend(line.split(';')) for line in lines if line]
    files = [quote_plus(file, safe='/:') for file in files]
    return files, not_available


def retrieve_from_sra(study_accession: str) -> list:
    search = rq.get(f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=sra&term={study_accession}&retmax=100000').content
    sra_ids = xmltodict.parse(search).get('eSearchResult', {}).get('IdList', {}).get('Id')
    file_urls = []
    run_info = xmltodict.parse(
                               rq.get(f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=sra&id={",".join(sra_ids)}').text)
    experiment_packages = run_info.get('EXPERIMENT_PACKAGE_SET').get('EXPERIMENT_PACKAGE')
    for experiment_package in experiment_packages:
        # For some reason sometimes it's a list and sometimes it's a dictionary
        runs = experiment_package.get('RUN_SET').get('RUN')
        if not isinstance(runs, list):
            runs = [runs]
        for run in runs:
            run_files = run.get('SRAFiles').get('SRAFile')
            if not isinstance(run_files, list):
                run_files = [run_files]
            for file in run_files:
                if file['@sratoolkit'] == '1':
                    continue
                if file.get('@url'):
                    file_urls.append(file.get('@url'))

    file_urls = [quote_plus(file, safe='/:') for file in file_urls]
    return (file_urls, []) if file_urls else retrieve_from_ena(study_accession)


def retrieve_file_urls(study_accession: str) -> list:
    """
    Given an ENA/GEO study or project accession, retrieve and return a list of all the ftp addresses for the files.

    :param study_accession: str
                            Accession for an ENA project or study (e.g. PRJEBXXXX)
    :returns files: list
                    List of all the ftp addresses for the files within the study/project.
    """
    if "PRJEB" in study_accession:
        source = "ena"
    elif "E-MTAB" in study_accession:
        source = "ae"
    else:
        source = "sra"

    # Calling different functions depending on source
    return globals()[f'retrieve_from_{source}'](study_accession)

def correct_filename_from_ena(run_accession, filename):

    while True:
        try:
            search = rq.get(f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=sra&term={run_accession}').content
            sra_id = xmltodict.parse(search).get('eSearchResult', {}).get('IdList', {}).get('Id')

            run_info = xmltodict.parse(rq.get(f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=sra&id={sra_id}').content)
            run_files = run_info.get('EXPERIMENT_PACKAGE_SET').get('EXPERIMENT_PACKAGE').get('RUN_SET').get('RUN')
            if isinstance(run_files, list):
                run_provisional = []
                for run in run_files:
                    run_provisional.append(run.get('SRAFiles').get('SRAFile'))
                run_files = run_provisional
            else:
                run_files = run_files.get('SRAFiles').get('SRAFile')
            break
        except ExpatError as e:
            print(f"Got error {e}. This is probably due to NCBI receiving too many requests at once. Waiting 1 s...")
            sleep(3)

    # If only 1 option, will return orderedDict instead of list. Correcting here
    if isinstance(run_files, OrderedDict):
        run_files = [run_files]

    # Get a list of all the filenames for that run accession
    filenames = [name.get('Alternatives', [{}])[0].get('@url').split('/')[-1] for name in run_files if name.get('@sratoolkit', "1") == '0']

    # Sometimes there are no filenames
    if not filenames:
        return filename

    # Check if R1 or R2
    if filename.endswith('_1.fastq.gz'):
        read_index = "1"
    elif filename.endswith('_2.fastq.gz'):
        read_index = "2"
    else:
        return filename

    # Search in the options
    real_filename = next(real_name for real_name in filenames if f"R{read_index}" in real_name)

    # Correct the ".1" at the end
    real_filename = real_filename.split('.1')[0] if real_filename.endswith('.1') else real_filename

    return real_filename


def define_source_parameters(path: str) -> (any([OpenerDirector, str]), int, str, str):
    """
    Finds and returns the source file parameters given a path.

    :param path: str
                 string that contains the path to the file (Currently accepted: ftp, s3, local)
    :returns streamable: any([OpenerDirector, str])
                         Entity that can be passed to smart_open to stream the file
    :returns file_size: int
                        Size of the file
    :returns filename: str
                       Name of the file
    :returns source: str
                     Source of the file. Currently accepted: ftp, s3, local.
    """
    if "ftp" in path:
        if not path.startswith("ftp://"):
            path = f"ftp://{path}"
        streamable = urlopen(path)
        file_size = int(streamable.headers['Content-length'])
        source = "ftp"

    elif "s3" in path:
        streamable = path
        s3 = boto3.resource('s3')
        bucket_name = path.split("/")[2].split('.')[0]
        key = "/".join(path.split("/")[-2:])
        s3_object = s3.Object(bucket_name, key)
        try:
            file_size = s3_object.content_length
        except ClientError:
            file_size = 1
        source = "s3"

    elif 'https://' in path:
        streamable = urlopen(path)
        file_size = int(streamable.headers['Content-length'])
        source = 'ftp'
    # Local files
    else:
        streamable = path
        file_size = os.stat(path).st_size
        source = "local"

    filename = path.split('/')[-1]
    if filename.endswith('.1'):
        filename = filename.strip('.1')

    if 'SRR' in filename:
        filename = correct_filename_from_ena(path.split('/')[-2], filename)

    return streamable, file_size, filename, source


def define_destination_parameters(output: str) -> str:
    """
    Define destination path (remote/local). Currently accepted: s3, local

    :param output: str
                   path to the output folder.
    :returns str
             "s3" or "local"
    """
    if output.startswith("s3"):
        return "s3"
    else:
        return "local"


def transfer_file(path: str, output: str) -> None:
    """
    General function to transfer the files. Takes a file path and an output folder.

    :param path: str
                 Path to the file to be transferred. Accepts s3, ftp and local, but needs to be a full path for remote.
    :param output: str
                   Path to the directory where the file will be transferred. Needs to be a full path for remote.
    """
    file_stream, file_size, filename, source = define_source_parameters(path)
    with op(file_stream, 'rb', ignore_ext=True) as f:
        globals()[f'transfer_file_to_{define_destination_parameters(output)}'](f, output, filename, file_size)


def transfer_file_to_local(origin: any([str, BytesIO]), destination: str, filename: str = '',
                           file_size: int = None) -> None:
    """
    Transfer a file from an origin to a remote destination.
    :param origin: any([str, OpenerDirector])
                   Path/streamable object pointing to a file.
    :param destination: str
                        path to the destination folder for the file
    :param filename: str
                     Name of the file
    :param file_size: int
                      Size of the file, in bytes.
    """
    if not filename:
        filename = origin.split('/')[-1]
    if isinstance(origin, str) and not origin.startswith('s3'):
        print("Please provide with a file stream as an origin.")
        return
    with open(f"{destination}/{filename}", "wb") as f:
        with origin as s:
            with tqdm(desc=filename, total=file_size, unit='B', unit_scale=True) as t:
                while True:
                    chunk = s.read(10 * 1024 * 1024)
                    if not chunk:
                        break
                    f.write(chunk)
                    t.update(len(chunk))


def transfer_file_to_s3(url: BytesIO, output_path: str, filename: str,
                        file_size: int = 0, prefix: str = 'hca-util-upload-area'):
    """
    Transfer file to an s3 bucket
    :param url: BytesIO
                BytesIO object that can be streamed.
    :param output_path: str
                output path
    :param prefix: str
                Bucket preffix, e.g. "hca-util-upload-area"
    :param filename: str
                Name of the file
    :param file_size: int
                      Size of the file
    """
    # Check if path ends with / or not and retrieve bucket key
    bucket = output_path.split('/')[-2] if output_path.endswith('/') else output_path.split('/')[-1]

    s3 = boto3.resource('s3')
    hca_util_upload = s3.Bucket(prefix)

    # Try to retrieve the file size from the source
    if not file_size:
        file_size = int(rq.head(url, stream=True).headers['content-length'])
        if file_size == 0:
            file_size = int(rq.head(url, stream=True).headers['Content-Length'])

    filename = unquote_plus(filename)
    full_filename = f"{bucket}/{filename}"

    # Check if file already exists in the bucket
    try:
        s3.Object(hca_util_upload.name, full_filename).load()
        print(f"File {filename} already exists in s3 bucket")
        return
    except:
        pass

    s3_client = boto3.client('s3')

    def hook(t):
        def inner(bytes_amount):
            t.update(bytes_amount)

        return inner

    while True:
        try:
            with tqdm(desc=filename, total=file_size, unit='B', unit_scale=True) as t:
                s3_client.upload_fileobj(url, hca_util_upload.name, full_filename, Callback=hook(t))
            break
        except KeyboardInterrupt:
            print("Detected interruption. Proceeding to end the upload...")
            break
        except:
            print("Retrying...")


def main(args):
    ena_list, runs_not_available = retrieve_file_urls(args.study_accession)
    if not ena_list:
        print("Couldn't find any mean of downloading the proper fastq. Try with the sratoolkit")

    if args.allowed is not None:
        try:
            with open(args.allowed, 'r') as f:
                lines = f.read().splitlines()
            filtered_ena_list = []
            for line in lines:
                filtered_ena_list.append(next((s for s in ena_list if line in s)))
            ena_list = filtered_ena_list

        except FileNotFoundError:
            print("File not found, please provide full path.")

    output_args = [(ena, args.output_path) for ena in ena_list]
    try:
        with Pool(args.threads) as p:
            p.starmap(transfer_file, output_args)
    except KeyboardInterrupt:
        print("Process has been interrupted.")
        p.terminate()

    if runs_not_available:
        print(f"The following Runs weren't available for download: {','.join(runs_not_available)}")


if __name__ == '__main__':
    parser_args = parse_args()
    main(parser_args)