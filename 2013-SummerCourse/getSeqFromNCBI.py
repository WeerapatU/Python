#description: this script is to fetch sequence from NCBI by Entrez
#usage: python getSeqFromNCBI.py input_file seq_format output_file
#bug report: joey0576@163.com

from Bio import Entrez
import sys

Entrez.email = "joey0576@163.com"

if len(sys.argv) !=4:
	print "*** "+"Usage: python getSeqFromNCBI.py input_file seq_format output_file"+" ***"
	print "*** " + "sequence format:fasta,gb "
	sys.exit(2)
else:
	inputfile = sys.argv[1]
	seqformat = sys.argv[2]
	outputfile = sys.argv[3]
	accessibleFormat = ["fasta","gb"]

	if seqformat not in accessibleFormat:
		print "format wrong: "+ seqformat +" is not accepted."
		print "accessible sequence format: fasta,gb"
	else:
		#read sequence identifiers
		idlist = open(inputfile)

		filecontent = ""
		for seqid in idlist:
			seqid = seqid.strip()
			if seqid:
				searchresult = Entrez.efetch(db="nucleotide", id=seqid, 
				rettype=seqformat, retmode="text")
				if filecontent:
					filecontent += searchresult.read()
				else:
					filecontent = searchresult.read()

		#write sequences to file
		output = open(outputfile,"w")
		output.write(filecontent)

		#close files
		idlist.close()
		output.close()


