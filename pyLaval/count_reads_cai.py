#!/user/bin/pythom

##this script is to process tophat accepted reads from ribosome data, 

import sys
import csv

## get uniq records from accepted hits csv file
def get_uniq(csv_content):
	uniq_list = []
	same_read = True
	for row in csv_content:
		if uniq_list == []:
			uniq_list.append(row)
		else:
			for item in uniq_list:
				for i in range(0, len(row)):
					if str(row[i]) == str(item[i]):
						#print row[i] +" ---- " + item[i]
						same_read = True
					else:
						same_read = False

		if same_read == False:
			#print same_read
			uniq_list.append(row)
		same_read = True

	write_out(list2string(uniq_list), outfile_name)

##convert list to string for output as text file
def list2string(my_list):
	string_content = ""
	for item in my_list:
		for i in range(0, len(item)):
			string_content += item[i] + "\t"
		string_content += "\n"

	return string_content

##write out file
def write_out(file_content, filename):
 	outfile = open(filename,"w")
 	outfile.write(file_content)
 	outfile.close()

## main program
infilename = sys.argv[1]
outfile = infilename.split(".")[0]
if "/" in outfile:
	outfile = outfile.split("/")[-1]
outfile_name = "uniq_" + outfile + ".csv"

#open file and get read it as csv
infile = open(infilename,"r")
csv_content = csv.reader(infile, delimiter="\t")

get_uniq(csv_content)

infile.close()
