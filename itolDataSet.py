#
#

import sys
import csv

 

def writeFile(output,filename):
	outputfile = open(filename, "w")
	outputfile.write(output)

	outputfile.close()

def clinicColor(fileContent):
	output1 = "" 
	filename1 = "dataset1_symptom.txt"
	for row in fileContent:
		if row[5] == "F":
			output1 += row[0] + "," + "#AE0000" + "\n"
		elif row[5] == "S":
			output1 += row[0] + "," + "#C6A300"+ "\n"
		elif row[5] == "M":
			output1 += row[0] + "," + "#0000E3"+ "\n"
		else:
			output1 += row[0] + "," + "#6C6C6C"+ "\n"
	
	writeFile(output1,filename1)

def monthColor(fileContent):
	output2 = ""
	filename2 = "dataset2_month.txt"
	for row in fileContent :
		if row[4] in ["Jan", "Feb", "Mar"]:
			output2 += row[0] + "," + "#BB3D00"+ "\n"
		elif row[4] in ["Apr", "May", "Jun"]:
			output2 += row[0] + "," + "#8F4586"+ "\n"
		elif row[4] in ["Jul", "Aug", "Sep"]:
			output2 += row[0] + "," + "#743A3A"+ "\n"
		elif row[4] in ["Oct", "Nov", "Dec"]:
			output2 += row[0] + "," + "#808040"+ "\n"
		else:
			output2 += row[0] + "," + "#6C6C6C"+ "\n"

	writeFile(output2,filename2)

def yearColor(fileContent):
	output3 = ""
	filename3 = "dataset3_year.txt"
	for  row in fileContent:
		if row[6] in ["1997", "1998","1999", "2000", "2001","2002", "2003"]:
			output3 += row[0] + "," + "#5B00AE"+ "\n"
		elif row[6] in ["2004", "2005", "2006", "2007"]:
			output3 += row[0] +"," + "#930093"+ "\n"
		elif row[6] in ["2008", "2009", "2010", "2011" ,"2012", "2013"]:
			output3 += row[0] + "," + "#BF0060"+ "\n"
		else:
			output3 += row[0] + "," + "#6C6C6C"+ "\n"
	writeFile(output3,filename3)

def originismColor(fileContent):
	output4 = ""
	filename4 = "dataset4_originism.txt"
	for  row in fileContent:
		if row[1] == "EV A71":
			output4 += row[0] +"," + "#005757"+ "\n"
		else:
			output4 += row[0] + "," + "#6C6C6C"+ "\n"

	writeFile(output4,filename4)

def provinceColor(fileContent):
	output5 = ""
	filename5 = "dataset5_province.txt"
	for  row in fileContent:
		##Eastern China/ East China/ huadong: shandong, jiangsu, anhui, zhejiang, fujian, shanghai
		if row[3] in ["SD", "JS", "AH","JX","ZJ","FJ","SH"]:
			output5 += row[0] +"," + "#EAC100"+ "\n" ## east china
		
		##huanan/ Sourthern China/South China: guangdong, guangxi, hainan
		elif row[3] in ["GD", "GX", ]:
			output5 += row[0] +"," + "#8080C0"+ "\n" ## sourthern china
		
		##huazhong/ Central China/ Center China:hubei, hunan, henan
		elif row[3] in ["HuB", "HeN"]:
			output5 += row[0] +"," + "#FF9224"+ "\n" ## central china
		
		##huabei/ North China:beijing, tianjing, hebei, shanxi,neimenggu
		elif row[3] in ["BJ", "", "JS","AH"]:
			output5 += row[0] +"," + "#73BF00"+ "\n"  # notrh china
		
		##xibei/ NorthWest China/ Northwesterner: ningxia, xinjiang, qinghai, shan'anxi,gansu
		elif row[3] in ["SAX", "GS"]:
			output5 += row[0] +"," + "#FFE153"+ "\n"  #northwest
		
		## Southwest China/ xinan: sochuan, yunnan, guizhou, xizang, chongqing
		elif row[3] in ["CQ"]:
			output5 += row[0] +"," + "#CCFF80"+ "\n"  # sourthwest
		
		## Northwest China/ dongbei:liaoning, jilin, heilongjiang
		elif row[3] in ["LN" ]:
			output5 += row[0] +"," + "#FF79BC"+ "\n"  #northwest
		
		else:
			output5 += row[0] + "," + "#6C6C6C"+ "\n"  ##ns

	# writeFile(output5,filename5)
	outputfile = open(filename5, "w")
	outputfile.write(output5)

	outputfile.close()

def mainblock():
	fileContent = csv.reader(open(sys.argv[1], "r"), delimiter = "\t")
	
	#clinicColor(fileContent)
	#monthColor(fileContent)
	#yearColor(fileContent)
	#originismColor(fileContent)
	provinceColor(fileContent)

if len(sys.argv) < 2:
	print "ERROR"
	print "Usage: python " + sys.argv[0] + "input_file"
else:
	mainblock()