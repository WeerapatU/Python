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
from  lxml import etree 

#usage: python $0 csv_file_with_orf_and_translation database_file

#os.chdir("/home/joey/research/s.cere/blast-20140930")

in_csv_file = sys.argv[1]
csv_file = open(in_csv_file,"r")

in_database_file = sys.argv[2]

csv_content = csv.reader(csv_file, delimiter=",")

new_row = ""
#os.sysyem('formatdb -i orf_coding.fasta -p F -a F -o T ')

def write_file(blastout):
	file_name = "./result/tmp_blast.xml"
	out_put = open(file_name, "w")
	out_put.write(blastout)
	out_put.close()
	return file_name

def list2string(thelist):
	tmp_string = ""
	for item in thelist:
		tmp_string += item +","
	return tmp_string

for row in csv_content:
	query_seq = row[6]
	tmp_seq = Seq(query_seq, generic_dna)
	blast_commandline = NcbiblastxCommandline( db="orf_trans_all.fasta ", evalue=0.001, outfmt=5, )
	blast_out,err = blast_commandline(query_seq)
	
	file_name = write_file(blast_out)

	blast_all_records = NCBIXML.parse(open(file_name,"r"))
	index = 0

	for record in blast_all_records:
		new_row += list2string(row)
		for alignment in record.alignments:
			index += 1
			for hsp in record.alignments:
				new_row += ("," + (hsp.title).replace(",", "."))
			if index == 3: break # get top 3 hit in blast result
		new_row += ("\n")
	#xml_file.close()

out_file_name = "./result/blast_filter_result.csv"
out_file_filter = open(out_file_name,"w")
out_file_filter.write(str(new_row))
out_file_filter.close()


csv_file.close()


