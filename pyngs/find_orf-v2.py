#!/user/bin/python

## this is to get all orf from genome, both starnd(+1, -1).
## Bug report to joey0576@163.com

import sys
from Bio import SeqIO  
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import re

## Standard genetic code
start_codon = ["ATG"]
end_codons = ["TGA", "TAA", "TAG"]

## Yest Mitochondrial code
end_Mit_codons = ["TAA", "TAG"]

## minimum threshold of orf length in aa sequnence
minimum_threshold = 75
## maximum threshold of orf length in dna sequence
maximum_threshold = 330

## function to find orfs in a sequence
def findOrfs(sequence,seq_len, tmp_end_codons, seq_info):
	found_start_codon = False
	start_codon_index = 0
	end_codon_index = 0
	orf_info = ""
	for i in range(0,3):
		for index in range(i, seq_len, 3):
			current_codon = sequence[index : index + 3]
			if current_codon in start_codon and not found_start_codon:
				found_start_codon = True
				start_codon_index = index
			if current_codon in tmp_end_codons and found_start_codon:
				end_codon_index = index
				orf_len = end_codon_index - start_codon_index +1

				if orf_len >= minimum_threshold and orf_len <= maximum_threshold:
					orf = sequence[start_codon_index : end_codon_index]
					
					tmp_translaton = ""
					
					if tmp_end_codons == end_codons:
						tmp_translaton = Seq(orf, generic_dna).translate(1)
					elif tmp_end_codons == end_Mit_codons:
						tmp_translaton = Seq(orf, generic_dna).translate(2)
						
					orf_info += seq_info + "," +  str(start_codon_index+1) +"," + str(end_codon_index) + "," + str(len(orf)) + "," + orf +"," + str(len(tmp_translaton))+ ","+ tmp_translaton + "\n"
					#orf_info +=  seq_info + "," +  str(start_codon_index+1) +"," + str(end_codon_index) + "," + str(len(orf)) + "," + orf +"," + str(len(tmp_translaton))+ ","+ tmp_translaton + "\n" 

					found_start_codon = False

        start_codon_index = 0
        end_codon_index = 0
        found_start_codon = False

	return orf_info

## write orf sequence and related informations to local file in csv file format
def output_as_csv(csv_file_name, csv_file_content):
	output = open(csv_file_name, "w")
	output.write(str(csv_file_content))
	output.close()

## output text file
def output_as_txt(text_file_name, text_file_content):
	output = open(text_file_name, "w")
	output.write(str(text_file_content))
	output.close()

## write orf sequences and related information to local file in fasta format.
def output_as_fasta(csv_file_content):
	## file name for saving dna and aa sequences to local file in fasta format
	dna_seq_filename = "altORFs_in_dna.fasta"
	aa_seq_filename = "altORFs_in_aa.fasta"
	## buffer to hold dna and aa sequences
	dna_seq_content = ""
	aa_seq_content = ""

	csv_file_content_lines = csv_file_content.split("\n")
	for i in range(0,len(csv_file_content_lines)):
		## values in every line of the csv file content, separated by ","
		row_val = csv_file_content_lines[i].split(",")
		## "F" for forwrd strand, value = "1"; "R" for reverse strand, value="-1"
		type(row_val[2])
		type_strand = "N"
		if row_val[2] == "1" :
			type_strand = "F"
		elif row_val[2] == "-1" :
			type_strand = "R"
		seq_accession = row_val[0] +"_"+ str(row_val[1]).replace(" ", "-") + "_"+str(row_val[3])+"_"+type_strand+"_"+str(row_val[4])
		dna_seq = str(row_val[6])
		aa_seq = str(row_val[8])
		dna_seq_content += ">"+seq_accession+"\n"+dna_seq +"\n"
		aa_seq_content += ">"+seq_accession +"\n"+aa_seq+"\n"
	## write out files
	output_as_txt(dna_seq_filename, dna_seq_content)
	output_as_txt(aa_seq_content, aa_seq_filename)



################### main program ####
if __name__ == "__main__":

	in_file = sys.argv[1]
	in_file_prefix = in_file.split(".")[0]
	# set output file name
	out_file = (in_file.split(".")[0]) + "_altORFs.csv"

	fasta_file = open(in_file, "r")

	all_orfs = ""

	for seqrecord in SeqIO.parse(fasta_file,"fasta"):
		seqrecord_accession = seqrecord.id
		
		seqrecord_seq = str(seqrecord.seq).upper()
		reverse_seqcord_seq = str(seqrecord.seq.reverse_complement()).upper()
		seq_len = len(seqrecord_seq)

		seqrecord_info = in_file_prefix +","+seqrecord_accession 

		## to regular expression to match mitochondrion sequence
		id_pattern = re.compile(r'chrM')
		id_match = id_pattern.match(seqrecord.id)

		if id_match:
			## mitochondrion in yeast
			all_orfs +=  findOrfs(seqrecord_seq, seq_len, end_Mit_codons, (seqrecord_info+","+"+1")) #
			all_orfs +=  findOrfs(reverse_seqcord_seq, seq_len, end_Mit_codons, (seqrecord_info+","+"-1"))
		else:
			## nuclear genome
			all_orfs +=  findOrfs(seqrecord_seq, seq_len, end_codons, (seqrecord_info+","+"+1") ) 
			all_orfs +=  findOrfs(reverse_seqcord_seq, seq_len, end_codons, (seqrecord_info+","+"-1"))

	## write out
	output_as_csv(out_file, all_orfs)
	output_as_fasta(all_orfs)

	fasta_file.close()
