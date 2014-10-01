#!/bin/python/

from Bio.Blast import NCBIWWW
from Bio.Blast import  NCBIXML
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Blast.Applications import NcbiblastxCommandline
import csv
import sys
import os
from Bio.Alphabet import generic_dna

tmp_dna = "ATGGCCCATCTCTCACTGAATCAGTACCAAATGCACTCACATCATTATGCACGGCACTTGCCTCAGCGGTCTATACCCTGTGCCATTTACCCA"
tmp_aa = "MAHLSLNQYQMHSHHYARHLPQRSIPCAIYP"

# result = NCBIWWW.qblast("blastn", "nr", tmp_dna)
# blast_records = NCBIXML.parse(result)
# for record in blast_records:
# 	for alignment in record.alignments:
# 		for hsp in alignment.hsps:
# 			print hsp.expect
# 			print alignment.title
# 			print alignment.length
# 			# print hsp.query
# 			# print hsp.match
# 			# print hsp.sbjct

# # print blast_records

#usage: python $0 csv_file_with_orf_and_translation database_file

os.chdir("/home/joey/research/s.cere/blast-20140930")

in_csv_file = sys.argv[1]
csv_file = open(in_csv_file,"r")

in_database_file = sys.argv[2]

csv_content = csv.reader(csv_file, delimiter=",")

#os.sysyem('formatdb -i orf_coding.fasta -p F -a F -o T ')

for row in csv_content:
	query_seq = row[6]
	tmp_seq = Seq(query_seq, generic_dna)
	blast_commandline = NcbiblastxCommandline(query= query_seq, db="orf_coding", evalue=0.001, outfmt=5, out="./tmp_result/blast_out.xml")
	os.system(str(blast_commandline))

	# xml_file = open("/tmp_result/blast_out.xml")
	# blast_records = NCBIXML.parse(xml_file)
	# for record in blast_records:
	# 	for hsp in record.alignments:
	# 		print hso.expect

	# xml_file.close()


csv_file.close()

