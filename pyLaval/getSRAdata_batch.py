#!/usr.bi/python

import sys
import os

infilename = sys.argv[1]

infile = open (infilename, "r")

def directGet(infile):
	
	for name in infile:
		name = name[0:-1]
		cmd_str = "wget ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR948/" + name +"/"+name+".sra" 
		os.system(cmd_str)

	
#get sra data via ftp path provrdered by summary file on ncbi.
def getFromSummary(infile):
	lines = infile.readlines()[1:] 
	for line in lines:
		url =  (line.split(",")[14])[1:-1]
		cmd_str = "wget " + url
		os.system(cmd_str)

###main program
#directGet(infilename)

getFromSummary(infile)

infile.close()