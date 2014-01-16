#thsi to filter sites varation. Avoiding using for loop in R, so use this python script to 
#	filter same amino acid sites.
#author:joey
#2014-01-06

import csv
import sys

def mainblock():
	inputfilename = sys.argv[1]
	outputfilename = sys.argv[2]

	fileContent = csv.reader(open(inputfilename, 'r'), delimiter="\t")
	output = ""
	for row in fileContent:
		fatalGroup = (row[1].split(","))[0].split(" ")[1] 
		severeGroup = (row[2].split(","))[0].split(" ")[1]
		mildGroup = (row[3].split(","))[0].split(" ")[1]  

		if fatalGroup == severeGroup and severeGroup == mildGroup:
			pass
		else:
			output += row[0] + "\t" + row[1] + "\t" + row[2] + "\t" +row[3] +"\n"

	print output
	outputfile = open(outputfilename,"w")
	outputfile.write(output)
	outputfile.close()


if len(sys.argv) < 3:
	print "ERROR"
	print "Usage: python siteVariationFilter.py input_file output_file"
else:
	mainblock()

