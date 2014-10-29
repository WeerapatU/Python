#!/user/bin/python

## this is use to blast two protein sequence.

from Bio.Blast import  NCBIXML
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Blast.Applications import NcbiblastpCommandline
import csv
import sys

query_in_file = sys.argv[1]
object_in_file = sys.argv[2]

querr_file = open(query_in_file,"r")
object_file = open(object_in_file,"r")

object_file_content = csv.reader(object_file, delimiter=",")

for row in csv.reader(querr_file, delimiter=","):
	## avoid last lien of the file
	if len(row) != 0:
		query_seq = row[12]
		for rowline in object_file_content:
			object_seq = rowline[15]
			blast_commandline = NcbiblastpCommandline( subject = object_seq , outfmt=5, )
			
			blast_out,err = blast_commandline(query_seq)
			print blast_out

querr_file.close()
object_file.close()


