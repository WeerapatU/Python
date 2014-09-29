#!/bin/python/

##todo: to simplify the code

import csv
import sys


in_file = sys.argv[1]
csv_file = open(in_file,"r")

csv_content = csv.reader(csv_file, delimiter=",")

y = 0.01

coordinate_orf = ""
chrosome_name = ["chr I","chr II","chr III","chr IV" ,"chr V","chr VI","chr VII","chr VIII","chr IX","chr X","chr XI","chr XII","chr XIII","chr XIV","chr XV","chr XVI","mit complet"]
chrosome_length = [230218,813184,316620,1531933,576874,270161,1090940,562643,439888,745751,666816,1078177,924431,784333,1091291,948066,85779]

for row in csv_content:
	for i in (range(0,len(chrosome_name))):
		if chrosome_name[i] in row[1]:
			if i ==0:
				coordinate_orf += str(row[3])+ ","+ str(y) + "\n"

			coordinate_orf += str(row[3])
	if "chr I" in row[1]:
		coordinate_orf += str(row[3]) + "," +str(y) + "\n"
		coordinate_orf += str(row[4]) + "," +str(y) + "\n"
	
	else:
		print "not chrsome I"230218

	coordinate_orf += str(row[3]) + "," +str(y) + "\n"
	coordinate_orf += str(row[4]) + "," +str(y) + "\n"
	y+= 0.01

output = open("Coordinates_in_orfs_map.csv","w")
output.write(str(coordinate_orf))

output.close()
csv_file.close()



