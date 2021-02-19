import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('file_name',type=str,help='path to file with the following columns: run,library,experiment,lib_protocol,seq_protocol')
args = parser.parse_args()

df = pd.read_csv(args.file_name,sep="\t")

rows = [[list(df['run'])[i],list(df['library'])[i],list(df['experiment'])[i],list(df['lib_protocol'])[i],list(df['seq_protocol'])[i],list(df['run'])[i] + '_1.fastq.gz','read1'] for i in range(0,len(list(df['run'])))]
df1 = pd.DataFrame(rows)

rows = [[list(df['run'])[i],list(df['library'])[i],list(df['experiment'])[i],list(df['lib_protocol'])[i],list(df['seq_protocol'])[i],list(df['run'])[i] + '_2.fastq.gz','read2'] for i in range(0,len(list(df['run'])))]
df2 = pd.DataFrame(rows)

df3 = df1.append(df2)

df3.to_csv('processed_sequence_tab.txt',sep='\t')
