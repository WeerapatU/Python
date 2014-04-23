#

import sys
import csv
from Bio import SeqIO
import re

def nameDir():
	fileContent = csv.reader(open(sys.argv[2], "r"), delimiter="\t")
	seqid_dict = {}
	for row in fileContent:
		### you can change here to build a new string using information from csv file 
		seqid_dict[row[0]] = row[0] + "_"+row[6]
	return seqid_dict
	

def mainRun():
	output = ""
	seqDict = nameDir()
	fastaFile = open(sys.argv[1])
	print str(fastaFile)
	for record in SeqIO.parse(fastaFile, "fasta"):
		#print record

		if record:
			print "yes"
		else:
			print "wrong"
		output += ">"+ seqDict[record.id] +"\n"+record.seq+"\n"
	fastaFile.close()
	filenames = (sys.argv[1]).split(".")
	newname = filenames[0] +"_3." +filenames[1]

	outputfile = open(newname,"w")
	outputfile.write(output)

	outputfile.close()

	
def mainRun2():
	output = ""
	seqDict = nameDir()
	fastaFile = open(sys.argv[1],"r")
	for line in fastaFile:
		output += line
	fastaFile.close()
	filenames = (sys.argv[1]).split(".")
	newname = filenames[0] +"_2." +filenames[1]

	for i in seqDict:
		regex = re.compile(i)
		output = regex.sub(seqDict[i], output)

	outputfile = open(newname,"w")
	outputfile.write(output)

	outputfile.close()

	


if len(sys.argv) < 3:
	print "ERROR"
	print "Usage: python " + sys.argv[0] + " fasta_sequenceFile nameInformation_csv"
else:
	mainRun()
	#mainRun2()