#!/usr/bin/python

##this script is to generate fasta format sequence fron csv files, which cintains altORFs information.

import sys
import csv

infilename = sys.argv[1]
infile = open(infilename,"r")


def write_out(filename, file_content):
	output = open(filename, "w")
	output.write(file_content)
	output.close()

for row in csv.reader(infile, delimiter=","):

	seq_name = ""
	
	seq_name = row[10]+"_"+row[11] +"_"+row[12] 
	
	seq_str = row[15]
	
	#write every sequence into individual file
	write_out(("./altORFs/"+ seq_name+".fasta"), ((">"+seq_name) +"\n" + seq_str))
	

infile.close()