#!/usr/bin/python

import csv
import sys

row_1 = " "+"\t"
row_2 = "-1"+"\t"
row_3 = "+1" +"\t"
infile = open((sys.argv[1]),"r")


def get_list(infilee):
	tmplist = []
	for row in csv.reader(infilee, delimiter="\t"):
		if row[1] not in tmplist:
			tmplist.append(row[1])
	return tmplist

def getcontent(line_dif,infileeee):
	row_2_list = [0]*len(line_dif)
	row_3_list = [0]*len(line_dif)

	
	for line in csv.reader(infileeee,delimiter="\t"):	
		tmpindex = line_dif.index(line[1])
		if line[2] =="-1":
			row_2_list[tmpindex] = line[0]
		
		if line[2] =="1":
			row_3_list[tmpindex] = line[0]

	file_contentt = list2txt(row_1,line_dif) +"\n" + list2txt(row_2,row_2_list) +"\n" + list2txt(row_3,row_3_list)+"\n"
	return file_contentt



	
def list2txt(txttxt,listlist):
	for i in range(len(listlist)):
		txttxt += str(listlist[i]) +"\t"
	return txttxt

line_diff = get_list(infile)

file_content= getcontent(line_diff,open((sys.argv[1]),"r"))

output = open("out_file.csv","w")
output.write(str(file_content))
infile.close()
output.close()

