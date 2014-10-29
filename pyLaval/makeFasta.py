#!/user/bin/python

##this is to make fasta sequence from csv file generated six frame orfs.

import sys
import csv
from Bio import SeqIO

in_file_name = sys.argv[1]
out_file = sys.argv[2]

in_file = open(in_file_name, "r")

read_csv = csv.reader(in_file,delimiter=",")

##save sequence in here
seq_pool = ""

for row in read_csv:
	if row[2] == "+1":
		title1 = row[0].split("_")[-1]
		title2 = row[1].split(" ")[0]+row[1].split(" ")[1]
		title3 = "f" +str(row[3]) + "t" + str(row[4])
		seq_string = row[6]
		seq_pool += ">" + title1 + "_" + title2 + "_" + title3 + "\n" + seq_string + "\n"

output = open(out_file, "w")
output.write(str(seq_pool))

output.close()
in_file.close()