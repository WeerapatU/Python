#
from Bio import SeqIO
import sys

def fastaTocsv():
	inputFileName = sys.argv[1]
	outputFileName = sys.argv[2]

	fasta_infile = open(inputFileName)
	seqInfo = ""
	for record in SeqIO.parse(fasta_infile,"fasta"):
		seqInfo += record.id 
		seqChar = (record.seq)

		i =0
		while i < (len(seqChar)):
			#print seqChar[i]
			seqInfo += "," + seqChar[i] 
			i +=1 
		else:
			#print "hello"
			seqInfo += "\n"

	output = open(outputFileName,"w")
	output.write(str(seqInfo))

	output.close() 
	fasta_infile.close()



if len(sys.argv) <3:
	print "ERROR"
	print "usage: python fastaToCsv.py input_fasta_file output_csv_file"
	sys.exit(2)
else:
	fastaTocsv()