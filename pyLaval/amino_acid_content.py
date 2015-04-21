#!/usr/bin/python

import sys
import Bio.SeqIO

## Apoloar:   'G','A','P','V','I','L','M','F','W'
## uncharged: 'S','T','C','N','Q','Y'
## charged polar: 'D','K','E','H','R'
amino_acid_list = ['G','A','P','V','I','L','M','F','W','S','T','C','N','Q','Y','D','K','E','H','R']

## normalization method 1 --- direct normalization
def normalization_1(nor_list):
	min_val = float(min(nor_list))
	max_val = float(max(nor_list))
	for i in range(0, len(nor_list)):
		nor_list[i] = (float(nor_list[i]) - min_val) / (max_val - min_val)
	return nor_list

## normalization method 2 --- canonical normalization
def normalization_2(nor_list):
	sum_val = float(len(nor_list))
	for i in range(0, len(nor_list)):
		nor_list[i] = (float(nor_list[i])) / sum_val
	return nor_list

##calculate amino acid content from csv file
## 9th columm in csv file is amino acid sequence
def aa_content_csv(csv_file):
	content_account_list = []
	content_account = [0]*20
	infile = open(csv_file,"r")
	for row in csv.reader(infile, delimiter=","):
		aa_seq = row[8]
		for i in range(0,20):
			content_account[i] = aa_seq.count(amino_acid_list[i])
			content_account_list.append(normalization_1(content_account))

## calculate amino acid content from fasta sequences file
def aa_content_fasta(fasta_file):
	content_account_list = []
	in_file = open(fasta_file, "r")
	for record in SeqIO.parse(infile,"fasta"):
		seq_id = record.id 
		seq_str = record.seq
		seq_account = [0] * 20
		for i in range(0,20): 
			seq_account[i] = seq_str.count(amino_acid_list[i])
			content_account_list.append(normalization_1(content_account))


## main program
input_file = sys.argv[1]


