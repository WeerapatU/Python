#2013-08-16
#joey
#usage : python txt2csv.py txtfilename csvfilename

import sys

infilename = sys.argv[1]
outfimename = sys.argv[2]

infile = open(infilename)
csvline = ""

for line in infile:
	splitList = line.split(" ")
	listlen = len(splitList)
	for i in range(0,listlen):
		if splitList[i].strip() != "":
			csvline += splitList[i] + ","

	csvline += "\n"

output = open(outfimename,"w")
output.write(csvline)

infile.close()
output.close()