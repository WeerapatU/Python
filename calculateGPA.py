#description: this script is writed to calculate GPA
#usage:
#author:joey 
#bug report:joey0576@163.com

import sys
import string

infile = open(sys.argv[1],"r")
creditSum =0
scoreSum =0
for line in infile:
	credit =0
	score = 0
	argv1 = ((line.split(",")[1]).replace(".", "", 1)).strip()
	argv2 = ((line.split(",")[2]).replace(".", "", 1)).strip()

	if argv1.isdigit() and argv2.isdigit():
		scoreSum += float(line.split(",")[1]) * float(line.split(",")[2])
		creditSum += float(line.split(",")[1])

gpa = (scoreSum*4)/(creditSum*100)
print scoreSum,creditSum,gpa
	# if argv1.isdigit() :
	# 	if float(line.split(",")[1]) >0 and float(line.split(",")[1]) <10:
	# 		credit = float(line.split(",")[1])
	# else :
	# 	if argv1 in ["A","B","C","D","E","F"]:

	# if 	argv2.isdigit() :
	# else:
	# 	print "gg"

	# print ((line.split(",")[1]).replace(".", "", 1)).isdigit()
	# print ((line.split(",")[2]).replace(".", "", 1)).strip()
	# print ((line.split(",")[2]).strip().replace(".", "", 1)).isdigit()

#replace(".", "", 1).isdigit()


	# if float(line.split(",")[1]) and float(line.split(",")[2]):
	# 	print "hello"

	# else:
	# 	if not float(line.split(",")[1]):
	# 		print line.split(",")[1]+"is a string"


	# 	elif not float(line.split(",")[2]):
	# 		print line.split(",")[2]+"is a string"

	#print float(line.split(",")[1]) * float(line.split(",")[2])
	#print line

infile.close()