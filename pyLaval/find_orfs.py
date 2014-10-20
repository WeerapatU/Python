#!/bin/python

## this is to get all orf(30-200 aa) from genome, both starnd(+1, -1).
#Bug report to joey0576@163.com

import sys
from Bio import SeqIO  
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import re

#function to find orfs in a sequence
def findOrfs(sequence,seq_len, tmp_end_codons, seq_info):
	found_start_codon = False
	start_codon_index = 0
	end_codon_index = 0

	for i in range(0,3):
		orf_info = ""
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
					
					 
					orf_info +=  seq_info + "," +  str(start_codon_index+1) +"," + str(end_codon_index) + "," + str(len(orf)) + "," + orf +"," + str(len(tmp_translaton))+ ","+ tmp_translaton + "\n" 
					#orf_info +=  tmp
					#orfs.append(found_start_codon)
				found_start_codon = False

        start_codon_index = 0
        end_codon_index = 0
        found_start_codon = False

	return orf_info


################### main program ####
in_file = sys.argv[1]
# out_file = sys.argv[2]

out_file = (in_file.split(".")[2]).split("/")[-1] + "_orfs.csv"

#Standard genetic code
start_codon = ["ATG"]
end_codons = ["TGA", "TAA", "TAG"]

#Yest Mitochondrial code
end_Mit_codons = ["TAA", "TAG"]

minimum_threshold = 90
maximum_threshold = 600

fasta_file = open(in_file)

all_orfs = ""

for seqrecord in SeqIO.parse(fasta_file,"fasta"):
	seqrecord_accession = seqrecord.id.split("_")[0]
	seqrecord_chrosome = seqrecord.id.split("_")[1] + " " + seqrecord.id.split("_")[2]
	seqrecord_seq = str(seqrecord.seq).upper()
	reverse_seqcord_seq = str(seqrecord.seq.reverse_complement()).upper()
	seq_len = len(seqrecord_seq)

	seqrecord_info = seqrecord_accession + "," + seqrecord_chrosome 

	#to regular expression to match mitochondrion sequence
	id_pattern = re.compile(r'mit')
	id_match = id_pattern.match(seqrecord.id)

	if id_match:
		## mitochondrion in yeast
		all_orfs +=  findOrfs(seqrecord_seq, seq_len, end_Mit_codons, (seqrecord_info+","+"+1")) #
		all_orfs +=  findOrfs(reverse_seqcord_seq, seq_len, end_Mit_codons, (seqrecord_info+","+"-1"))
	else:
		## nuclear genome
		all_orfs +=  findOrfs(seqrecord_seq, seq_len, end_codons, (seqrecord_info+","+"+1") ) 
		all_orfs +=  findOrfs(seqrecord_seq, seq_len, end_codons, (seqrecord_info+","+"-1"))

output = open(out_file,"w")
output.write(str(all_orfs))

output.close()
fasta_file.close()
