#!/bin/python

import sys
from Bio import SeqIO

#print "Usage: python $0 fasta_file "

in_file = sys.argv[1]

fasta_file = open(in_file, "r")

all_len = 0

for seqroad in SeqIO.parse(fasta_file, "fasta"):
	print seqroad.id + "," + str(len(seqroad.seq))
	all_len += len(seqroad.seq)

print "Total length," + str(all_len)

fasta_file.close()
