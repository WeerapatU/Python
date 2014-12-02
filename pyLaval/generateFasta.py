#!/usr/bin/python

##this script is to generate fasta format sequence fron csv files, which cintains altORFs information.

import sys
import csv

infilename = sys.argv[1]
infile = open(infilename,"r")

#sequence pool
dna_seq_content = ""
protein_seq_content = ""

def write_out(filename, file_content):
	output = open(filename, "w")
	output.write(file_content)
	output.close()

for row in csv.reader(infile, delimiter=","):

	seq_name = ""
	if row[1] == "+1":
		seq_name =  row[0]+"_F_"+row[2] +"_"+row[3]
	else:
		seq_name = ">"+ row[0]+"_R_"+row[2] +"_"+row[3]
	dna_seq = row[5]
	protein_seq = row[7]
	#add sequence to sequence pool
	dna_seq_content += seq_name +"\n" + dna_seq+"\n"
	protein_seq_content += seq_name +"\n" + protein_seq +"\n"
	#write every sequence into individual file
	write_out(("./dna_seq/"+seq_name+".fasta"), ((">"+seq_name) +"\n" + dna_seq))
	write_out(("./protein_seq/"+seq_name +".fasta"), ((">"+seq_name) +"\n" + protein_seq))

#write all sequences from sequence pool to file
write_out("all_dna_altORFs.fasta", dna_seq_content)
write_out("all_protein_altORFs.fasta", protein_seq_content)


infile.close()