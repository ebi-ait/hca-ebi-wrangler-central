
import smart_open
import boto3
import pandas as pd
from Bio import SeqIO
import argparse
import os

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--uuids', help='.txt file with hca-util submission uuids (uuid only). 1 uuid per line')
    parser.add_argument('--num_reads', default= 1000, help='number of reads to test')

    args = parser.parse_args()

    # Check if path ends with / or not and retrieve bucket key
    bucket_name = 'hca-util-upload-area'

    uuids = pd.read_csv(args.uuids,header=None)
    uuids = list(uuids[0])

    for uuid in uuids:

        s3 = boto3.resource('s3')
        my_bucket = s3.Bucket(bucket_name)
        keys = ['s3://hca-util-upload-area/' + str(s3_object.key) for s3_object in my_bucket.objects.all()]
        filenames = [key for key in keys if uuid in key]
        filenames = filenames[1:]

        my_dict = {}
        for filename in filenames:
            my_dict[filename] = {}
            with smart_open.open(filename) as f:
                count = 0
                len_seqs = []
                records = SeqIO.parse(f, 'fastq')
                for record in records:
                    if count < args.num_reads:
                        len_seqs.append(len(str(record.seq)))
                        count += 1
                    else:
                        break
                len_uniq = list(set(len_seqs))
                for uniq in len_uniq:
                    num = len_seqs.count(uniq)
                    my_dict[filename].update({uniq: num})

        data = pd.DataFrame.from_dict(my_dict, orient='index')
        out_file = uuid + "_read_lengths.txt"
        data.to_csv(out_file,sep="\t")
        print("Done processing uuid: %s" % (uuid))

if __name__ == "__main__":
    main()
