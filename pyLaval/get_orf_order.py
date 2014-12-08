#!/usr/bin/python

import sys
import re
import csv
from Bio import SeqIO

infilename = sys.argv[1]

infile = open(infilename, "r")

maxLen = 0

for record in SeqIO.parse(infile,"fasta"):
	tmp_len = len(record.description.split(","))
	if tmp_len > maxLen:
		maxLen = tmp_len

print maxLen
infile.close()

