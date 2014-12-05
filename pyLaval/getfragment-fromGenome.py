#!usr/bin/python

import sys
import csv
from Bio import SeqIO
from Bio.Alphabet import generic_dna
from Bio.Seq import Seq

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

##get rever complement sequence
def seq_rever_complement(sequence_string):
	dna_seq = Seq(sequence_string, generic_dna)
	reverse_seq = dna_seq.reverse_complement()
	return str(reverse_seq)

##write out
def write_out(filename, filecontent):
	output = open(filename, "w")
	output.write(filecontent)
	output.close()

##get genome dictionary
genome_dict = read_Genome(genome_infilename)

##sequence pool
filecontent = ""

for line in csv.reader(csv_infile, delimiter=","):
	orfID = line[0]
	position = line[2]
	chroms_name = position.split(":")[0]
	start_number, end_number = position.split(":")[1].split("-")
	if chroms_name in genome_dict.keys():
		#this orf is on forward sequence
		if start_number < end_number:
			dnaSeq = str(genome_dict[chroms_name])[(int(start_number)-1):int(end_number)]
			filecontent += ">" + orfID +"-F"+"\n"+dnaSeq+"\n"
		#this orf is on the reverse complement sequence
		else:
			tmp_seq = str(genome_dict[chroms_name])[(int(end_number)-1):int(start_number )]
			dnaSeq = seq_rever_complement(tmp_seq)
			filecontent += ">" + orfID +"-R"+"\n"+dnaSeq+"\n"

	else:
		print chroms_name + "	is not found in genome file.Have a check."
	

write_out("fasta_orf.fasta", filecontent)


csv_infile.close()