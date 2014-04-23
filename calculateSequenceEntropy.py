#this script is calculate the entropy of sequences
#2014-02-19

from Bio import SeqIO
import sys
import numpy as np
import math
from sets import Set

def convertAlignment2(alignment):  #convert single alignment file
	seqLen = 0
	#while seqLen >1:
	for record in SeqIO.parse(alignment, "fasta"):
		seqLen = len(record.seq)
	#break
	seqSymbols = [""]*seqLen
	for record in SeqIO.parse(alignment, "fasta"):
		tmpseq =""
		for i in range(seqLen):
			seqSymbols[i] += record.seq[i]
		#seqSymbols.append(tmpseq)

	return seqSymbols

def entropy(string):  #calculate entory of every sequence
	strinLsit = list(string)
	uniqstringlist = list(Set(strinLsit))
	frequenceList =[]
	for symbol in uniqstringlist:
		ctr = 0
		for i in strinLsit:
			if symbol == i:
				ctr += 1
		frequenceList.append(float(ctr)/len(strinLsit))

	ent = 0.0000
	for freq in frequenceList:
		ent  = ent + freq*math.log(freq,2)
	enr = -ent
	return ent

def conservation(output):
	consveredSites = ""
	lines = output.split("\n")
	for i in range(len(lines)):
		if i != 0:
			tmp = lines[i].split(",")
			if tmp
			consveredSites += 
		else:
			consveredSites += lines[0]




def mainRun2():  #process single alignment file
	alignmentFile = sys.argv[1]
	symbolList = convertAlignment2(alignmentFile)
	#print symbolList
	output = ""
	for i in range(len(symbolList)):
		entOfSeq = entropy(symbolList[i])
		output += "site"+str(i +1) + ","+str(entOfSeq) + "\n"

	outputfile = open("entropy_of_alignment.txt","w")
	outputfile.write(output)

	#alignmentFile.close()
	outputfile.close()


def mainRun():   # process more than two alignment files
	fileIndex = 0
	filenames = []
	namepiefix = []
	output  = "sites"
	while (fileIndex < len(sys.argv)-1):
		filenames.append(sys.argv[fileIndex +1])
		namepiefix.append((sys.argv[fileIndex +1]).split(".")[0])
		output += "," +(sys.argv[fileIndex +1]).split(".")[0]
		fileIndex += 1
	#break
	output += "\n"

	##check length of alignment
	length = 0
	for i in filenames:
		seqLen = [] ##sequence length in one alignment file 
		seqlength = [] ## sequence length from different alignment file
		alignment = open(i,"r")
		for record in SeqIO.parse(alignment,"fasta"):
			seqLen.append(str(len(record.seq)))
			uniq = list(Set(seqLen))
			if len(uniq) != 1:
				print "ERROR: alignment in different length"
				sys.exit(2)
		seqlength.append(seqLen[0])
		if len(list(Set(seqlength))) != 1:
			print "ERROR: alignment in different length"
			sys.exit(2)
		else :
			length = int(seqlength[0])
		alignment.close()
	
	fileList = []
	for i in filenames:
		#alignmentfile = open(i, "r")
		fileList.append(convertAlignment2(i))
		#alignmentfile.close()

	for i in range(length):
		output +="site" + str(i+1)
		for j in range(len(filenames)):
			output += "," + str(entropy(fileList[j][i]))
		output += "\n"

	conserved = conservation(output)
	consvered_outputfile = open("entropy_of_alignment-conserved.txt","w")
	consvered_outputfile.write(conserved)
	consvered_outputfile.close()

	outputfile = open("entropy_of_alignment.txt","w")
	outputfile.write(output)
	outputfile.close()



if len(sys.argv) < 2:
	print "ERROR"
	print "Usage: python " + sys.argv[0] + " alignment_sequence_file "
if len(sys.argv) ==2:
	#print "single"
	mainRun2()   #process single alignment file
else:
	mainRun()    # process more than two alignment files
	 
