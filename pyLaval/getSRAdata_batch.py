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
		accept_str = line.split(",")[0][1:-1]+".sra"
		cmd_str = "wget -r --accept " +accept_str +" --level 2  " + url
		os.system(cmd_str)

#get sra files from accession list file.
def getByAccession(infile):
	for line in infile:
		accession = line[0:-1]
		url =  "ftp://ftp-trace.ncbi.nih.gov"
		###/sra/sra-instant/reads/ByRun/sra/{SRR|ERR|DRR}/<first 6 characters of accession>/<accession>/<accession>.sra
		path = "/sra/sra-instant/reads/ByRun/sra/SRR/%s/%s/%s.sra" %(accession[0:6], accession, accession)
		os.system("wget " +url+path)
		
###main program
#directGet(infilename)

#getFromSummary(infile)

getByAccession(infile)

infile.close()