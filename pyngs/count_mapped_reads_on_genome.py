#!usr/bin/python

## description: this script is use to analysis bowtie2 result.
##				read sam file, count how many mapped reads on nucleotide position on genome.
##				as a measument of translation and transcript.

## usage: python script_name genome_file_name sam_file_names
##			sam_file_names can be just one file name, or a list of sam file names.
##			can handle single(merge several sam files to single sam file) or multi sam files.
##			the genome file is reference genome for bowtie2 mapping

import sys
from Bio import SeqIO

genome_infilename = sys.argv[1]

sam_infilenames = sys.argv[2:]

genome_dictionary = {}

##read genome file, build a list for every chrosome
## @return a dictionary, chromosome name as key, list as value
def genome_size(infilename):
	genome_dict = {}
	genome_in = open(infilename, "r")
	for record in SeqIO.parse(genome_in, "fasta"):
		chr_name = record.id
		chr_len = len(record.seq)
		tmp_list = [0]*chr_len
		genome_dict[chr_name] = tmp_list

	genome_in.close()
	return genome_dict

## open every sam file, and read, extract mapped position
def process_sam(sam_filename):
	sam_file = open(sam_filename,"r")
	for line in sam_file:
		line_elements = line.split("\t")
		## strand	chrosomename	start_position sequence seq_len
		## [1]		[2]				[3]				[9]		len([9])
		##[1]	---	16	-->	reverse strand
		##			4	-->	no reported alignments
		##			0	-->	
		##			1	-->	one of a pair
		##			2	-->	one end of a proper paired-end alignment
		##			8	-->	one of a pair and has no reported alignments
		##			32	-->	the paired-end alignment is aligned to the reverse reference strand
		##			64	-->	the first (#1) mate in a pair
		##			128	-->	the second (#2) mate in a pair
		##ignore head of sam file
		## every alignment line has 11 mandatory fields.
		if len(line_elements) >= 11:
			query_key = line_elements[2]
			if line_elements[1] == "16":
				#print "hello i am test"
				for i in range(int(line_elements[3]), (int(line_elements[3])+len(line_elements[9]) +1)):
					#print genome_dictionary[query_key][i]
					genome_dictionary[query_key][i] += 1
					#print genome_dictionary[query_key][i]
			elif line_elements[1] == "0":
				#print "hello i am test2"
				for j in range((int(line_elements[3]) - len(line_elements[9])), int(line_elements[3])):
					#print genome_dictionary[query_key][j]
					genome_dictionary[query_key][j] += 1
					#print genome_dictionary[query_key][j]


			 


def normalization():
	keys = genome_dictionary.keys()
	for key in keys:
		tmp_list = genome_dictionary[key]
		min_reads = float(min(tmp_list))
		max_reads = float(max(tmp_list))
		for i in range(len(tmp_list)):
			genome_dictionary[key][i] = (float(genome_dictionary[key][i]) - min_reads)/(max_reads - min_reads)

	#todo

##write the dictionary to local
def write_out():
	##gey all keys in the dictionary
	keys = genome_dictionary.keys()
	##
	for key in keys:
		tmp_list = genome_dictionary[key]
		print tmp_list
		##
		tmp_content = ""
		for i in range(len(tmp_list)):
			tmp_content += str(i+1) + "\t" + str(tmp_list[i]) + "\n"
		##every chromosome name as part of the file name
		filename = key + "_count_reads_on_chr.csv"
		##write out the list
		output = open(filename, "w")
		output.write(tmp_content)
		output.close()
	

def test():
	print "hello, this is a test"

## main program

test()

genome_dictionary = genome_size(genome_infilename)

for sam_infile in sam_infilenames:
	process_sam(sam_infile)

normalization()
write_out()