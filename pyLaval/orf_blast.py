#!/bin/python/

from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO,Seq


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

