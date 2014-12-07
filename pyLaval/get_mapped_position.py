#!user/bin/python

import sys
import csv

infilename = sys.argv[1]

infile = open(infilename,"r")

def get_position_from_sam(infile):
	for line in infile:
		print len(line.split("\t"))

get_position_from_sam(infile)

infile.close()