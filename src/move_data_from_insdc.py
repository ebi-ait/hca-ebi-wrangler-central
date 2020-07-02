import boto3
import os
from tqdm import tqdm
from smart_open import open as op
import requests as rq
import argparse
from urllib.request import urlopen
from urllib.request import OpenerDirector
from multiprocessing import Pool
from io import BytesIO


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
    parser.add_argument('--output_path', "-o", default='',
                        help='path where files will be downloaded: can be local or s3')
    parser.add_argument('--threads', "-t", default=1, type=int,
                        help='Number of processes to simultaneously spam')

    return parser.parse_args()


def retrieve_file_urls(study_accession: str) -> list:
    """
    Given an ENA/GEO study or project accession, retrieve and return a list of all the ftp addresses for the files.

    :param study_accession: str
                            Accession for an ENA project or study (e.g. PRJEBXXXX)
    :returns files: list
                    List of all the ftp addresses for the files within the study/project.
    """
    field = "submitted_ftp" if "PRJ" in study_accession else "fastq_ftp"
    request_url = (f"https://www.ebi.ac.uk/ena/data/warehouse/filereport?accession={study_accession}"
                   f"&result=read_run&fields={field}")
    request = rq.get(request_url)
    lines = request.text.splitlines()[1:]
    files = []
    [files.extend(line.split(';')) for line in lines]
    return files


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
        bucket_name = path.split("/")[2]
        key = "/".join(path.split("/")[-2:])
        s3_object = s3.Object(bucket_name, key)
        file_size = s3_object.content_length
        source = "s3"

    # Local files
    else:
        streamable = path
        file_size = os.stat(path).st_size
        source = "local"

    filename = path.split('/')[-1]

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
        if define_destination_parameters(output) == "s3":
            bucket_name = output.split("/")[-1]
            transfer_file_to_s3(f, bucket_name, filename=filename, file_size=file_size)
        else:
            transfer_file_to_local(f, output, filename, file_size)


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


def transfer_file_to_s3(url: BytesIO, bucket: str, filename: str, prefix: str = 'hca-util-upload-area',
                        file_size: int = None):
    """
    Transfer file to an s3 bucket
    :param url: BytesIO
                BytesIO object that can be streamed.
    :param bucket: str
                Key for the bucket, e.g. c4xxx5c4-dxxc-4xx8-8cc1-8xx0652xxxba
    :param prefix: str
                Bucket preffix, e.g. "hca-util-upload-area"
    :param filename: str
                Name of the file
    :param file_size: int
                      Size of the file
    """
    s3 = boto3.resource('s3')
    hca_util_upload = s3.Bucket(prefix)

    # Try to retrieve the file size from the source
    if not file_size:
        file_size = int(rq.head(url, stream=True).headers['content-length'])
        if file_size == 0:
            file_size = int(rq.head(url, stream=True).headers['Content-Length'])

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
    ena_list = retrieve_file_urls(args.study_accession)
    output_args = [(ena, args.output_path) for ena in ena_list]
    try:
        with Pool(args.threads) as p:
            p.starmap(transfer_file, output_args)
    except KeyboardInterrupt:
        print("Process has been interrupted.")
        p.terminate()


if __name__ == '__main__':
    parser_args = parse_args()
    main(parser_args)
