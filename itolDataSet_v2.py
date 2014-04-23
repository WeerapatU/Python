#
#

import sys
import csv

 

def writeFile(output,filename):
	outputfile = open(filename, "w")
	outputfile.write(output)

	outputfile.close()

def clinicColor(row):
	output = ""
	# for row in fileContent:
	if row[5] == "F":
		output += row[0] + "," + "#AE0000" + "\n"  #RGB 174, 0, 0
	elif row[5] == "S":
		output += row[0] + "," + "#C6A300"+ "\n"   #RGB 198, 163, 0
	elif row[5] == "M":
		output += row[0] + "," + "#0000E3"+ "\n"   #RGB 0, 0, 227
	else:
		output += row[0] + "," + "#6C6C6C"+ "\n"    #RGB 
	
	# writeFile(output1,filename1)
	return output

def monthColor(row):
	output = ""
	# for row in fileContent :
	if row[4] in ["Jan", "Feb", "Mar"]:
		output += row[0] + "," + "#BB3D00"+ "\n"   #RGB 187, 61, 0
	elif row[4] in ["Apr", "May", "Jun"]:
		output += row[0] + "," + "#8F4586"+ "\n"   #RGB 143, 69, 134
	elif row[4] in ["Jul", "Aug", "Sep"]:
		output += row[0] + "," + "#743A3A"+ "\n"   #RGB 116, 58, 58
	elif row[4] in ["Oct", "Nov", "Dec"]:
		output += row[0] + "," + "#808040"+ "\n"   #RGB 128, 128, 64
	else:
		output += row[0] + "," + "#6C6C6C"+ "\n"   #RGB 108, 108, 108

	# writeFile(output2,filename2)
	return output

def yearColor(row):
	output = ""
	# for  row in fileContent:
	if row[6] in ["1997", "1998","1999", "2000", "2001","2002", "2003"]:
		output += row[0] + "," + "#5B00AE"+ "\n"   #RGB 91, 0, 174
	elif row[6] in ["2004", "2005", "2006", "2007"]:
		output += row[0] +"," + "#930093"+ "\n"     #RGB 147, 0, 147
	elif row[6] in ["2008", "2009", "2010", "2011" ,"2012", "2013"]:
		output += row[0] + "," + "#BF0060"+ "\n"    #RGB 191, 0, 96
	else:
		output += row[0] + "," + "#6C6C6C"+ "\n"
	#writeFile(output3,filename3)
	return output

def originismColor(row):
	output = ""
	# for  row in fileContent:
	if row[1] == "EV A71":
		output += row[0] +"," + "#005757"+ "\n"   #RGB 0, 87, 87
	else:
		output += row[0] + "," + "#6C6C6C"+ "\n"

	# writeFile(output4,filename4)
	return output

def provinceColor(row):
	output = ""
	# for  row in fileContent:
	##Eastern China/ East China/ huadong: shandong, jiangsu, anhui, zhejiang, fujian, shanghai
	if row[3] in ["SD", "JS", "AH","JX","ZJ","FJ","SH"]:
		output += row[0] +"," + "#EAC100"+ "\n" ## east china        #RGB 234, 193, 0
	
	##huanan/ Sourthern China/South China: guangdong, guangxi, hainan
	elif row[3] in ["GD", "GX", ]:
		output += row[0] +"," + "#8080C0"+ "\n" ## sourthern china   #RGB 128, 128, 192
	
	##huazhong/ Central China/ Center China:hubei, hunan, henan
	elif row[3] in ["HuB", "HeN"]:
		output += row[0] +"," + "#FF9224"+ "\n" ## central china      #RGB 255, 146, 36
	
	##huabei/ North China:beijing, tianjing, hebei, shanxi,neimenggu
	elif row[3] in ["BJ", "", "JS","AH"]:
		output += row[0] +"," + "#73BF00"+ "\n"  # notrh china          #RGB 115, 191, 0
	
	##xibei/ NorthWest China/ Northwesterner: ningxia, xinjiang, qinghai, shan'anxi,gansu
	elif row[3] in ["SAX", "GS"]:
		output += row[0] +"," + "#FFE153"+ "\n"  #northwest           #RGB  255, 225, 83
	
	## Southwest China/ xinan: sochuan, yunnan, guizhou, xizang, chongqing
	elif row[3] in ["CQ"]:
		output += row[0] +"," + "#CCFF80"+ "\n"  # sourthwest        #RGB  204, 255, 128
	
	## Northwest China/ dongbei:liaoning, jilin, heilongjiang
	elif row[3] in ["LN" ]:
		output += row[0] +"," + "#FF79BC"+ "\n"  #northwest           #RGB 255, 121, 188
	
	else:
		output += row[0] + "," + "#6C6C6C"+ "\n"  ##ns

	return output

def mainblock():
	fileContent = csv.reader(open(sys.argv[1], "r"), delimiter = "\t")
	
	output1 = "" zho
	filename1 = "dataset1_symptom.txt"
	output2 = ""
	filename2 = "dataset2_month.txt"
	output3 = ""
	filename3 = "dataset3_year.txt"
	output4 = ""
	filename4 = "dataset4_originism.txt"
	output5 = ""
	filename5 = "dataset5_province.txt"

	for row in fileContent:
		output1 += clinicColor(fileContent)
		output2 += monthColor(fileContent)
		output3 += yearColor(fileContent)
		output4 += originismColor(fileContent)
		output5 +=  provinceColor(fileContent)

	writeFile(output1,filename1)
	writeFile(output2,filename2)
	writeFile(output3,filename3)
	writeFile(output4,filename4)
	writeFile(output5,filename5)


if len(sys.argv) < 2:
	print "ERROR"
	print "Usage: python " + sys.argv[0] + "input_file"
else:
	mainblock()