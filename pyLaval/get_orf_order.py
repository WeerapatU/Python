#!/usr/bin/python

import sys
import re
import csv
from Bio import SeqIO

##process the sgd orf file, in fasta format.
def process_sgd_orf(infilename):
	sgd_orf_list = []
	infile = open(infilename, "r")

	for record in SeqIO.parse(infile,"fasta"):
		description = record.description
		chr_pat = r"Chr\s[A-Za-z]{1,5}"
		posit_pat = r"[0-9]{1,9}-[0-9]{2,9},"
		posit_match = re.findall(posit_pat,description)
		chr_match = re.search(chr_pat,description)

		chro_name = ""
		##if have matched chromosome
		if chr_match:
			chr_name = chr_match.group(0)
			num = chr_name.split(" ")[1]
			if num == "Mito":
				chro_name = "chrM"
			else:
				chro_name =  "chr"+num

		##match start and end position
		if posit_match:
			for record in posit_match:
				record = record[0:-1]
			# 	##chrosome_name, start_position, end_position
				start = int(record.split("-")[0] )
				end = int(record.split("-")[1])
				if (start-end) >30 or (end -start)> 30:
					tmp_list = [chro_name, record.split("-")[0], record.split("-")[1]]
					sgd_orf_list.append(tmp_list)

	infile.close()
	return sgd_orf_list

def process_altorf(infilename):
	infile = open(infilename, "r")
	altorf_list = []
	for line in csv.reader(infile,delimiter=","):
		chr_name, positions= line[2].split(":")
		start,end = positions.split("-")

		##orf_name, chromosome_name, start position, end_position, value
		tmp_list = [line[0], chr_name, int(start), int(end),0]
		altorf_list.append(tmp_list)

	infile.close()
	return altorf_list

def find_order(sgd_list, alt_list):
	for i in range(len(alt_list)):
		start_alt = int(alt_list[i][2])
		end_alt = int(alt_list[i][3])
		
		for item_j in sgd_list:
			
			if alt_list[i][1] == item_j[0]:
				start_sgd = int(item_j[1])
				end_sgd = int(item_j[2])
				if start_sgd < end_sgd:
					tmp_range = range(start_sgd,(end_sgd+1))
					etmp_range_l = range((start_sgd-99),start_sgd)
					etmp_range_r = range((end_sgd+1),(end_sgd+101))
					if start_alt in tmp_range and end_alt in tmp_range:
						alt_list[i][4] = 0
					elif start_alt in etmp_range_l or end_alt in etmp_range_l:
						alt_list[i][4] = -1
					elif start_alt in etmp_range_r or end_alt in etmp_range_r:
						alt_list[i][4] = 1

				else:
					range(end_sgd,(start_sgd+1))
					tmp_range = range(end_sgd,(start_sgd+1))
					etmp_range_l = range((end_sgd-99),start_sgd)
					etmp_range_r = range((end_sgd+1),(start_sgd+101))
					if start_alt in tmp_range and end_alt in tmp_range:
						alt_list[i][4] = 0
					elif start_alt in etmp_range_l or end_alt in etmp_range_l:
						alt_list[i][4] = -1
					elif start_alt in etmp_range_r or end_alt in etmp_range_r:
						alt_list[i][4] = 1
	return alt_list

def write_out(filename, file_ontent):
	output = open(filename, "w")
	output.write(file_ontent)
	output.close()

def list2txt(inlist):
	tmp_content = ""
	for item in inlist:
		for itemj in item:
			tmp_content += str(itemj) +"\t"
		tmp_content += "\n"
	return tmp_content
####main program

list1 = process_sgd_orf(sys.argv[1])
list2 = process_altorf(sys.argv[2])				
filecotent_list = find_order(list1, list2)
write_out("orf_order.csv", list2txt(filecotent_list))

