
# How to run:

#Requirements:
#Bio
#pandas

# python get_dummy_fastq.py [input_file_path]
# or: python get_dummy_fastq.py [input_file_path] [output_directory_path]
# default output directory: "dummy_files"
# input file is required; list of required gzipped fastq files (no header).

# import required python modules

import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import argparse
import os
import subprocess
from subprocess import check_call

# function to check validity of input file

def check_file(path):
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError("file %s does not exist" % (path))
    try:
        df = pd.read_csv(path, sep="\t", header=None)
    except:
        raise argparse.ArgumentTypeError("file %s is not a valid format" % (path))
    try:
        names = list(df.loc[:,0])
    except:
        raise argparse.ArgumentTypeError("file %s is not a valid format" % (path))
    return names
    
# parse command-line arguments

parser = argparse.ArgumentParser()
parser.add_argument('input_file',type=check_file,help='path to input .txt file with fastq file names (no header)')
parser.add_argument('--output_dir',default='dummy_files/',
                    help='path to output directory; if it does not exist, the directory will be created')

args = parser.parse_args()

# main body of code to create the required gzipped fastq files

# get the required fastq file names from the input file
names = args.input_file

# check if the specified output directory exists; if not, create it
if not os.path.exists(args.output_dir):
	os.mkdir(args.output_dir)
	output_dir = args.output_dir
else:
	output_dir = args.output_dir

# for each name in the list of file names, create a dummy fastq file with dummy sequence and quality scores
for name in names:

	record = SeqRecord(id="dummy_read",description="",seq=Seq("ACGAC"))
	record.letter_annotations["phred_quality"] = [26,26,26,26,26]
	
  # process the file names and paths
  tmp = os.path.join(output_dir,name)
	name = name.split(".gz")[0]
	output_path = os.path.join(output_dir,name)
	print("creating file %s" % (tmp))
	
  # write file to the output directory
  with open(output_path, "w") as output_handle:
    		SeqIO.write(record, output_handle, "fastq")
	check_call(['gzip', output_path])
