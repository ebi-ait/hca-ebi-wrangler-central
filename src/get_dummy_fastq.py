
# How to run:

# python get_dummy_fastq.py [input_file_path]
# or: python get_dummy_fastq.py [input_file_path] -o [output_directory_path]
# default output directory: "dummy_files"
# input file is required; list of required gzipped fastq files (no header).

import argparse
import os
import gzip

FASTQ_DUMP = ("@SRR001666.1 071112_SLXA-EAS1_s_7:5:1:817:345 length=36\n"
              "GGGTGATGGCCGCTGCCGATGGCGTCAAATCCCACC\n"
              "+SRR001666.1 071112_SLXA-EAS1_s_7:5:1:817:345 length=36\n"
              "IIIIIIIIIIIIIIIIIIIIIIIIIIIIII9IG9IC")

def load_file_content(path):
    try:
        with open(path, "r") as f:
            names = f.read().splitlines()
        assert all([name.endswith(".fastq.gz") for name in names])
    except FileNotFoundError:
        raise argparse.ArgumentTypeError(f"file {path} does not exist")
    except AssertionError:
        raise argparse.ArgumentTypeError(f"file {path} does not contain fastq.gz filenames with a valid format")

    return names

def parse_args():

    # parse command-line arguments

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', type=load_file_content,
                        help='path to input .txt file with list of fastq.gz file names, each on a new line with '
                             'no header.')
    parser.add_argument('--output_dir', "-o", default='dummy_files/',
                        help='path to output directory, by default creates a directory "dummy_files" in current working '
                             'directory. If output directory does not exist, it will be created.')

    args = parser.parse_args()

    return args

def main(args):
    # main body of code to create the required gzipped fastq files

    # get the required fastq file names from the input file
    names = args.input_file

    # check if the specified output directory exists; if not, create it
    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)
        output_dir = args.output_dir
    else:
        output_dir = args.output_dir

    # Create a binary representation of the fastq content to write it directly with gzip
    binary_content = bytearray(FASTQ_DUMP, encoding="utf-8")

    # for each name in the list of file names, create a dummy compressed fastq file
    for name in names:
        filename = os.path.join(output_dir, name)
        with gzip.open(filename, "wb") as f:
            f.write(binary_content)
        print(f"Created file {filename.split('/')[-1]}")


if __name__ == '__main__':
    args = parse_args()
    main(args)
