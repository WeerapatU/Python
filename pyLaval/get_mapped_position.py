#!user/bin/python

##line in sam files

# SRR1258539.6
# 16	
# chrXII	
# 461824	
# 255	
# 14S37M	
# *	
# 0	
# 0	
# GATGGTGCCTACAGGGTAGTGGTATTTCACTGGCGCCGAAGCTCCCACTTA	
# HIIHHDFGIIGIGIFBBD?GAHJIIIFHFHHGEIIHIGHFFHFFEDBD@@?	
# AS:i:74	
# XN:i:0	
# XM:i:0	
# XO:i:0	
# XG:i:0	
# NM:i:0	
# MD:Z:37	
# YT:Z:UU

##lines in csv file
#sORF-19,XLOC_003307+,chrXV:38888-39046,N/A,100,3.00E-26,105,N.D.,33.96,0.005,37,N.S.,0,-,-,-,0,-,-,-,0,-,-,-,0,-,-,-,0,-,-,-,0,-,-,-,0,-,-,-



import sys
import csv

infilename = sys.argv[1]

infile = open(infilename,"r")

def get_position_from_sam(infile):
	all_mapped_content = ""
	for line in infile:
		## strand	chrosomename	start_position sequence seq_len
		## [1]		[2]				[3]				[9]		len([9])
		line_group = line.split("\t")
		if line_group[2].startwith("chr"):
			tmp = line_group[1]+","+line_group[2]+","+line_group[3]+","+line_group[9]+","+str(len(line_group[9]))+"\n"
			all_mapped_content += tmp
		#print len(line.split("\t"))

	return all_mapped_content

def combine_to_orf(mapped_reads, orf_dict):
	for line in mapped_reads:
		line_group = line.split(",")
		if line_group[1] in orf_dict.keys():
			if line_group[2] > orf_dict[line_group[1]][1]:
				if line_group[2] < orf_dict[line_group[1]][2]:
					orf_dict[line_group[1]][3] = 

def orf_into_dict(orf_infile):
	orf_dict = {}
	for line in orf_infile:
		line_group = lien.split(",")
		chroso_name, position= line_group[2].split(":")
		start_p , end_p = position.split("-")

		orf_dict{chroso_name} = [line_group[0], start_p, end_p, 0]
	return orf_dict


get_position_from_sam(infile)

infile.close()