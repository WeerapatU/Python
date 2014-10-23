#!/usr/bin/python

#calculate cai in altORFs

import sys
import csv
from Bio.SeqUtils import CodonUsage
import math

SharpEcoliIndex = {
                    'GCA': 0.586, 'GCC': 0.122, 'GCG': 0.424, 
                    'GCT': 1,     'AGA': 0.004, 'AGG': 0.002, 
                    'CGA': 0.004, 'CGC': 0.356, 'CGG': 0.004, 
                    'CGT': 1,     'AAC': 1,     'AAT': 0.051, 
                    'GAC': 1,     'GAT': 0.434, 'TGC': 1, 
 					'TGT': 0.5,   'CAA': 0.124, 'CAG': 1, 
 					'GAA': 1,     'GAG': 0.259, 'GGA': 0.01, 
 					'GGC': 0.724, 'GGG': 0.019, 'GGT': 1, 
 					'CAC': 1,     'CAT': 0.291, 'ATA': 0.003, 
 					'ATC': 1,     'ATT': 0.185, 'CTA': 0.007, 
 					'CTC': 0.037, 'CTG': 1,     'CTT': 0.042, 
 					'TTA': 0.02,  'TTG': 0.02,  'AAA': 1, 
 					'AAG': 0.253, 'ATG': 1,     'TTC': 1, 
 					'TTT': 0.296, 'CCA': 0.135, 'CCC': 0.012, 
 					'CCG': 1,     'CCT': 0.07,  'AGC': 0.41, 
 					'AGT': 0.085, 'TCA': 0.077, 'TCC': 0.744, 
					'TCG': 0.017, 'TCT': 1,     'ACA': 0.076, 
					'ACC': 1,     'ACG': 0.099, 'ACT': 0.965, 
					'TGG': 1,     'TAC': 1,     'TAT': 0.239, 
					'GTA': 0.495, 'GTC': 0.066, 'GTG': 0.221, 
					'GTT': 1} 

sequence_string = "ATCGTATAGAATTCACCGGCT"

sequence_string = sequence_string.upper()

# cai_sum, cai_length = 0,0

def calcul_cai(sequence_string):
	cai_sum, cai_length = 0,0
	for i in range(0, len(sequence_string),3):
		codon = sequence_string[i:i+3]
		if codon in SharpEcoliIndex:
			if codon not in ['ATG', 'TGG']:
				cai_sum += math.log(SharpEcoliIndex[codon])
				cai_length += 1
		elif codon not in ['TGA', 'TAA', 'TAG']:
			raise TypeError("illegal codon in sequences")

	cai_value = math.exp(cai_sum / (cai_length - 1.0))
	return cai_value

def get_sequence_from_csv(infilename):
	csv_file = open(infilename,"r")
	for row in csv.reader(csv_file):
		print calcul_cai(row[6])
	
	csv_file.close()

def write_out(filename, filecontent):
	output = open(filename, "w")
	output.write(filecontent)
	output.close()

infilename = sys.argv[1]
outfile = infilename.split(".")[0]
if "/" in outfile:
	outfile = outfile.split("/")[-1]
outfile_name = "cai_" + outfile + ".csv"

get_sequence_from_csv(infilename)


# print cai_value
# cai_index = SharpEcoliIndex
# cai = cai_for_gene(sequence_string)
# print cai
