#!usr/bin/python

import sys
import csv
from Bio import SeqIO

csv_infilename = sys.argv[1]
genome_infilename = sys.argv[2]

csv_infile = open(csv_infilename, "r")

def read_Genome(genome_infilename):
	genome_infile = open(genome_infilename,"r")
	seq_dict = {}
	for seqrecord in SeqIO.parse(genome_infile,"fasta"):
		chromos = seqrecord.id 
		print chromos+","
		seq = seqrecord.seq 
		seq_dict[str(chromos)] = str(seq)
	genome_infile.close()
	return seq_dict

def write_out(filename, filecontent):
	output = open(filename, "w")
	output.write(filecontent)
	output.close()

genome_dict = read_Genome(genome_infilename)

filecontent = ""
for line in csv.reader(csv_infile, delimiter=","):
	orfID = line[0]
	position = line[2]
	chroms_name = position.split(":")[0]
	start_number, end_number = position.split(":")[1].split("-")
	print chroms_name
	dnaSeq = str(genome_dict[chroms_name])[(int(start_number)-1):int(end_number)]

	filecontent += ">" + orfID +"\n"+dnaSeq+"\n"

write_out("fasat_orf.fasta", filecontent)


csv_infile.close()