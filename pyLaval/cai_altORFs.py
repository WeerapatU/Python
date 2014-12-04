#!/usr/bin/python

#calculate cai in altORFs

import sys
import csv
from Bio.SeqUtils import CodonUsage
import math
import os
from Bio import SeqIO 

#codon index for E.Coli
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

#codon index for Yeast
SharpYeastIndex = {
                    'GCA': 0.015, 'GCC': 0.316, 'GCG': 0.001, 
                    'GCT': 1,     'AGA': 1, 	'AGG': 0.003, 
                    'CGA': 0.002, 'CGC': 0.002, 'CGG': 0.002, 
                    'CGT': 0.137, 'AAC': 1,     'AAT': 0.053, 
                    'GAC': 1,     'GAT': 0.554, 'TGC': 0.077, 
 					'TGT': 1,	  'CAA': 1,		'CAG': 0.007, 
 					'GAA': 1,     'GAG': 0.016, 'GGA': 0.002, 
 					'GGC': 0.020, 'GGG': 0.004, 'GGT': 1, 
 					'CAC': 1,     'CAT': 0.245, 'ATA': 0.003, 
 					'ATC': 1,     'ATT': 0.823, 'CTA': 0.039, 
 					'CTC': 0.003, 'CTG': 0.003, 'CTT': 0.006, 
 					'TTA': 0.117, 'TTG': 1,  	'AAA': 0.135, 
 					'AAG': 1,	  'ATG': 1,     'TTC': 1, 
 					'TTT': 0.113, 'CCA': 1,     'CCC': 0.009, 
 					'CCG': 0.002, 'CCT': 0.047, 'AGC': 0.031, 
 					'AGT': 0.021, 'TCA': 0.036, 'TCC': 0.693, 
					'TCG': 0.005, 'TCT': 1,     'ACA': 0.012, 
					'ACC': 1,     'ACG': 0.006, 'ACT': 0.921, 
					'TGG': 1,     'TAC': 1,     'TAT': 0.071, 
					'GTA': 0.002, 'GTC': 0.831, 'GTG': 0.018, 
					'GTT': 1} 

#test sequence string
sequence_string = "ATCGTATAGAATTCACCGGCT"
sequence_string = sequence_string.upper()

# cai_sum, cai_length = 0,0

def GC_count(sequence_string):
	gc_count = 0
	for i in range(0,len(sequence_string)):
		if str(sequence_string[i]) == "G" or str(sequence_string[i]) == "C":
			gc_count += 1
	tmp_gc = (gc_count/float(len(sequence_string)))
	return tmp_gc


#calculate cai in sequence string, return cai value
def calcul_cai(sequence_string):
	cai_sum, cai_length = 0,0
	for i in range(0, len(sequence_string),3):
		codon = sequence_string[i:i+3]
		# print codon

		#print SharpYeastIndex[str(codon)]
		# cai_sum += math.log(SharpYeastIndex[str(codon)])
		# cai_length += 1
		if str(codon) in SharpYeastIndex:
			cai_sum += math.log(SharpYeastIndex[str(codon)])
			cai_length += 1
			# if codon not in ['ATG', 'TGG']:
			# 	cai_sum += math.log(SharpYeastIndex[codon])
			# 	cai_length += 1
			# 	print "hello"
		#elif codon not in ['TGA', 'TAA', 'TAG']:
			#raise TypeError("illegal codon in sequences")
	#print str(cai_sum) +"---"+str(cai_length)
	cai_value = math.exp(cai_sum / (cai_length - 1.0))
	return cai_value

##calculate cai in sequence string, return cai value
## SPECIAL FOR RNA-SEQ DATA!
##TODO
def calcul_caiRibo(sequence_string):
	cai_sum, cai_length = 0,0
	for i in range(0, len(sequence_string),3):
		codon = sequence_string[i:i+3]
		if codon in SharpYeastIndex:
			if codon not in ['ATG', 'TGG']:
				cai_sum += math.log(SharpYeastIndex[codon])
				cai_length += 1
		elif codon not in ['TGA', 'TAA', 'TAG']:
			raise TypeError("illegal codon in sequences")

	cai_value = math.exp(cai_sum / (cai_length - 1.0))
	return cai_value

#get sequence string from a csv file, ans then call calcul_cai to calculate cai
#   return sequence lenght and cai value
def get_sequence_from_csv(infilename):
	new_file_content = ""
	csv_file = open(infilename,"r")
	for row in csv.reader(csv_file, delimiter=","):
		cai_row = calcul_cai(row[6])
		if row[2] != "-1":
			new_file_content += row[5] + "," + str(cai_row) + "\n"
	
	csv_file.close()
	return new_file_content

def get_sequence_chromosome(infilename):
	#list to save chromosome name
	chromosome_list = []
	# list to save altORF length and cai value in every chromosome
	chromosome_content_list = []
	#initial 
	new_chromosome_content = ""
	# open file 
	csv_file = open(infilename, "r")
	# read file as csv file
	for row in csv.reader(csv_file, delimiter=","):
		#calculation cai
		cai_row = calcul_cai(row[6])
		
		if row[1] in chromosome_list:
			#if chromosome name already exist, add to existed record, for the line item in file,
			#  will add after the for loop
			new_chromosome_content += row[5] + "," + str(cai_row) +"\n"
		else:
			# add new chromosome to the list
			chromosome_list.append(row[1])
			
			if new_chromosome_content != "":
				chromosome_content_list.append(new_chromosome_content)
				# clear for the next new chromosome
				new_chromosome_content = ""
				new_chromosome_content += row[5] + "," + str(cai_row) +"\n"
			#first record in file
			else:
				new_chromosome_content += row[5] + "," + str(cai_row) +"\n"

	chromosome_content_list.append(new_chromosome_content)
	## write out
	for i in range(0, (len(chromosome_list))) :
		write_out(str("./" + outfile + "/chr" + str(i +1) + ".csv"), chromosome_content_list[i])

	csv_file.close()

## use this to calculation CAI in tophat accepted hits. 
def calculate_caiRibo(infilename):
	new_content = ""
	# open file 
	csv_file = open(infilename, "r")
	# read file as csv file
	for row in csv.reader(csv_file, delimiter="\t"):
		#calculation cai
		cai_row = calcul_cai(str(row[3]))
		new_content += row[0] + "\t" + row[1] +"\t" +row[2] +"\t"+str(cai_row) +"\t"+row[3] +"\n"

	write_out(outfile_name, new_content)
	csv_file.close()

#calculate cai from mapped result file, .sam format.
def calculate_inSAM(infilename):
	new_content = ""
	# open file 
	csv_file = open(infilename, "r")
	# read file as csv file
	for row in csv.reader(csv_file, delimiter="\t"):
		#calculation cai
		
		cai_row = calcul_cai(str(row[9]))
		new_content += row[0] + "\t" + row[2] +"\t" +row[3] +"\t"+str(cai_row) +"\t"+row[9] +"\n"

	write_out(outfile_name, new_content)
	csv_file.close()

##for reads of ribosome profiling data, we do not know where is the start codon
##	so, calculate 3 frame ofthe reads, and use average of 3 frame cai value as cai of read.
def calculate_inReads(infilename):
	new_content = ""
	# open file
	csv_file = open(infilename, "r")
	# read file as csv file
	for row in csv.reader(csv_file, delimiter="\t"):
		cai_row = (calcul_cai(str(row[9][0:-1])) + calcul_cai(str(row[9][1:-1])) + calcul_cai(str(row[9][2:-1])) ) / 3
		##to do 
		new_content += row[0] + "\t" + row[2] +"\t" +row[3] +"\t"+str(cai_row) +"\t"+row[9] +"\n"
	##write out the output
	write_out(outfile_name, new_content)
	csv_file.close()

#calculate cai on single fasta file
#@infilename	input fasta file name
#@return 	sequence length and cai based on this sequence  
def calcuate_onFasta(infilename):
	fasta_file = open(infilename, "r")
	for seqrecord in SeqIO.parse(fasta_file,"fasta"):
		seq_cai = calcul_cai(seqrecord.seq)
		seq_len = len(seqrecord.seq)
		gc_count = GC_count(seqrecord.seq)
		return [seq_len, seq_cai,gc_count]
	fasta_file.close()

def calcuate_onMultiFasta(infilename):
	fasta_file = open(infilename, "r")
	filecontent = ""
	for seqrecord in SeqIO.parse(fasta_file,"fasta"):
		seq_cai = calcul_cai(seqrecord.seq)
		seq_len = len(seqrecord.seq)
		gc_count = GC_count(seqrecord.seq)
		filecontent += str(seqrecord.id) +"," + str(gc_count)+ "," + str(seq_cai) + "\n"
	write_out("cai_orf.csv",filecontent)
	fasta_file.close()

#give a fasta file name list, calculate cai on every fasta sequence file.
#@infilename	input file list text file.
#@
def calculate_fastaFiles(infilename):
	out_content = ""
	#infilename is the file of fasta sequences list
	infile = open(infilename ,"r")
	for line in infile:
		fasta_filename = line[0:-1]
		seq_len, seq_cai, gc_count = calcuate_onFasta(fasta_filename)
		out_content += str(seq_len/3) +"," + str(gc_count)+ "," + str(seq_cai) + "\n"

	write_out("cai_on_fasta.csv", out_content)
	infile.close()


#write file out
def write_out(filename, filecontent):
	output = open(filename, "w")
	output.write(filecontent)
	output.close()

### main program ### 
infilename = sys.argv[1]
outfile = infilename.split(".")[0]
if "/" in outfile:
	outfile = outfile.split("/")[-1]
outfile_name = "cai_" + outfile + ".csv"

##calculate CAI in whole genome
#filecontent = get_sequence_from_csv(infilename)
#write_out(outfile_name, filecontent)

##calculate CAI in every chromosome
#os.system("mkdir -p " + outfile)
#get_sequence_chromosome(infilename)

##calculate CAI in ribosome data and RNA-Seq data
##    tophat accepted hits
#calculate_caiRibo(infilename)

##calculate cai from mapped .sam file
#calculate_inSAM(infilename)

##calculate cai from reads file
#calculate_inReads(infilename)

##calculate cai on a list of fasta files
#calculate_fastaFiles(infilename)

##
calcuate_onMultiFasta(infilename)
