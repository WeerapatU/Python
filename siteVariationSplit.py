#
#
import sys
import csv
import re

def mainblock():
	fileContent = csv.reader(open((sys.argv[1]), "r"), delimiter = "\t")
	output = ""
	for row in fileContent:
		rowList = []
		for i in [row[1], row[2], row[3]]:
			if "," in i:
				igroup = i.split(",")
				for j in igroup:
					rowList.append(j[-1])
			else:
				rowList.append(i[-1])
		rowSet = set(rowList)
		
		for k in rowSet:
			siteChar = k
			fatalNum = ""
			severeNum = ""
			mildNum = ""

			#fatal column
			if siteChar in row[1]:
				if "," in row[1]:
					cellItems1 = (row[1]).split(",")
					for item1 in cellItems1:
						#print item1
						if siteChar in item1:
							fatalNum = item1[:-1]
				else:
					fatalNum = (row[1])[:-1]
			else:
				fatalNum = "0" 
			
			# severe culomn
			if siteChar in row[2]:
				if "," in row[2]:
					cellItems2 = (row[2]).split(",")
					for item2 in cellItems2:
						if siteChar in item2:
							severeNum = item2[:-1]
				else:
					severeNum = (row[2])[:-1]
			else:
				severeNum = "0"

			##mild column
			if siteChar in row[3]:
				if "," in row[3]:
					cellItems3 = (row[3]).split(",")
					for item3 in cellItems3:
						if siteChar in item3:
							mildNum = item3[:-1]
				else:
					mildNum = (row[3])[:-1]
			else:
				mildNum = "0"


			output += row[0] + "/" + siteChar + "," + fatalNum +","+severeNum+","+mildNum+"\n"

	## write output to file
	inputFileName = (sys.argv[1]).split(".")
	filename = inputFileName[0] + "_splited." + inputFileName[1]
	outputfile = open(filename, "w")
	outputfile.write(output)

	outputfile.close()


if len(sys.argv) < 2:
	print "ERROR"
	print "Usage: python " + sys.argv[0] + "input_file"
else:
	mainblock()
