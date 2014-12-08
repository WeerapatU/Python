#!use/bin/python

##get full information from ORFs file from SGD database.

from Bio import SeqIO
import sys


infilename = sys.argv[1]

infile = open(infilename, "r")

maxLen = 0

for record in SeqIO.parse(infile,"fasta"):
	#print record.id
	#print record.description
	tmp_len = len(record.description.split(","))
	if tmp_len > maxLen:
		maxLen = tmp_len

print maxLen
infile.close()

