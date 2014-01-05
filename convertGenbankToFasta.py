##description: this script is write to extract information from genbank file
##              outout file content ",", so use "\t" to separate information item.
#usage: python extractInfo.py infile_gb outfile
#bug report: joey0576@163.com

from Bio import SeqIO
import sys

if len(sys.argv) < 2:
	print "Usage: python extractInfo_v2.py your_genbank_file output_file_name"
	sys.exit(2)
else:
	#extract information from gb file

	infile = sys.argv[1]
	outfile = sys.argv[2]

	# if len(sys.argv) == 4:
	# 	lengthFilter = sys.argv[3]

	gbinfile = open(infile)
	seqInfo = ""
	for seqrecord in SeqIO.parse(gbinfile,"genbank"):
		
		# seq_accession = seqrecord.id.split(".")[0]
		# seq_version  = seqrecord.id.split(".")[1]   #id ,version
		# seq_gi = seqrecord.annotations["gi"]  #gi
		# seq_seq = seqrecord.seq   # sequence
		# seq_length = len(seqrecord.seq)
		# seq_desc = seqrecord.description #sequence description

		seqInfo += ">" + seqrecord.id.split(".")[0] + "\n" + seqrecord.seq  +"\n"

	output = open(outfile,"w")
	output.write(str(seqInfo))

	output.close()
	gbinfile.close() 
