#!/bin/python

import sys
import csv

in_file_name = sys.argv[1]
out_file_name = "filtered_blast_result.csv"

in_file = open(in_file_name,"r")

new_row = ""

def list2string(thelist):
	tmp_string =""

	for item in thelist:
		tmp_string += item +","
	return tmp_string

for row in csv.reader(in_file,delimiter=","):
	if len(row) == 12:
		new_row += list2string(row) + "\n"

output = open(out_file_name,"w")
output.write(new_row)

output.close()
in_file.close()