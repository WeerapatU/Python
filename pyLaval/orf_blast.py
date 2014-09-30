#!/bin/python/

from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO,Seq
from Bio.Blast.Applications import NcbiblastxCommandline
import csv
import sys

tmp_dna = "ATGGCCCATCTCTCACTGAATCAGTACCAAATGCACTCACATCATTATGCACGGCACTTGCCTCAGCGGTCTATACCCTGTGCCATTTACCCA"
tmp_aa = "MAHLSLNQYQMHSHHYARHLPQRSIPCAIYP"

result = NCBIWWW.qblast("blastn", "nr", tmp_dna)
blast_records = NCBIXML.parse(result)
for record in blast_records:
	for alignment in record.alignments:
		for hsp in alignment.hsps:
			print hsp.expect
			print alignment.title
			print alignment.length
			# print hsp.query
			# print hsp.match
			# print hsp.sbjct

# print blast_records

#usage: python $0 csv_file_with_orf_and_translation database_file
in_csv_file = sys.argv[1]
csv_file = open(in_file,"r")

in_database_file = sys.argv[2]

csv_content = csv.reader(csv_file, delimiter=",")

for row in csv_content:
	equery_seq = row[6]
	

