#
#change sequence id with more information
#author:joey
#2014-01-02
import sys
import csv
import re

if len(sys.argv) <4:
	print "ERROR!"
	print "USAGE: python seqID_replace.py source_file "
	sys.exit(2)
else:
	input_file = sys.argv[1]
	regfile = sys.argv[2]
	outoutfile =sys.argv[3]

	### function to build a dictionary that contsist old sstring and new string 
	def getRexRule():
		regfile_reader = csv.reader(open(regfile, 'r'), delimiter=",")
		seqid_dict = {}
		for row in regfile_reader:
			### you can change here to build a new string using information from csv file 
			seqid_dict[row[0]] = row[0] + "_"+row[1]+"_"+row[2]
		return seqid_dict

	seqId_dict = getRexRule()

	### function : read file and save as a text for replace
	def getFileContentASText():
		enquiry = open(input_file)
		file_content = ""
		for line in enquiry:
			file_content += line
		return file_content
		enquiry.close()

	textContent = getFileContentASText()

	for i in seqId_dict:
		regex = re.compile(i)
		textContent = regex.sub(seqId_dict[i], textContent)

	outout_to_file = open(outoutfile, "w")
	outout_to_file.write(textContent)

	outout_to_file.close()