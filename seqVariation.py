#
#### 描述：
#此脚本用于统计氨基酸序列在同一位点的差异情况。
#通过将同一位点氨基酸写成文本再调用shell来实现。

#用于序列操作
from Bio import SeqIO
#用于读取参数
import sys
#用于调用系统命令，shell
import os

fatal_seqs = []
severe_seqs = []
mild_seqs =[]
seqLen = 0

#根据序列的ID来对序列进行分类。序列id格式为EU703814_F_2008
def seqGrouping():
	inputFileName = sys.argv[1]
	outputFileName = sys.argv[2]

	fasta_infile = open(inputFileName)
	seqInfo = ""
	for record in SeqIO.parse(fasta_infile,"fasta"):
		seqInfo += record.id 
		#seqLen = len(record.seq)
		clintype = (record.id).split("_")[1]
		
		if clintype == "F":
			fatal_seqs.append(record)
		elif clintype == "S":
			severe_seqs.append(record)
		elif clintype =="M":
			mild_seqs.append(record)


		#print record
		

	# output = open(outputFileName,"w")
	# output.write(str(seqInfo))

	# output.close() 
	fasta_infile.close()

#创建目录。若该目录已存在，推出
def mkDir(folderName):
	# folderName = folderName.strip()
	# folderName = folderName.rstrip("\\")
	isExist = os.path.exists(folderName)
	if not isExist:
		os.makedirs(folderName)
	else:
		print "ERROR: path is already exists."
		sys.exit(2)

#将同一类型的序列抽取相同位点的氨基酸存为文本文件
def toSiteFiles(pathType,seqList):
	i = 0
	seqLen = len(seqList[0].seq)
	while i < (len(seqList[0].seq)):
		siteContent = ""
		for seqRecord in seqList:
			siteContent += (seqRecord.seq)[i] + "\n"

		outputfilename = pathType + "/" + "site" + str(i+1)+".txt" 
		output = open(outputfilename, "w")
		output.write(siteContent)

		output.close()

		i += 1

	else:
		print "done"

#调用命令统计相同位点氨基酸的差异性，并解析结果
def countVariation(textFile):
	command = "sort -g " + textFile + " | uniq -c"
	strInSTDOUT = os.popen(command).read()
	#strInSTDOUT = strInSTDOUT.rstrip("\\")
	strFeedback = ""
	for j in (strInSTDOUT.split("\n")):
		if j != "":
			j = j.strip()
			strFeedback += j + ","
	#print strInSTDOUT
	strFeedback = strFeedback.rstrip(",")
	return strFeedback

#调用上面的函数，输出结果
def countLoop(pathi):
	i = 0
	output = ""
	while i < 2193:
		filename = pathi + "/" + "site" + str(i +1) + ".txt"
		#$print countVariation(filename)
		#print "hello"
		output += "site" + str(i +1) + "\t" + countVariation(filename) + "\n"
	#print output
		i += 1
	else:
		outputfile = open((pathi[2:] + "_sites_variation.txt"),"w")
		outputfile.write(output)

		outputfile.close()



def proprocessing():
	#fatal
	mkDir("./fatal")
	toSiteFiles("./fatal", fatal_seqs)
	#print seqLen
	countLoop("./fatal")

	mkDir("./severe")
	toSiteFiles("./severe", severe_seqs)
	countLoop("./severe")
# 
	mkDir("./mild")
	toSiteFiles("./mild", mild_seqs)
	countLoop("./mild")
	




## main block
if len(sys.argv) <3:
	print "ERROR"
	print "usage: python fastaToCsv.py input_fasta_file output_csv_file"
	sys.exit(2)
else:
	seqGrouping()
	proprocessing()
	
	#countVariation("site1.txt")
