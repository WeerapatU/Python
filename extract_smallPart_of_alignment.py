##description: 
#usage: python namereplace.py infile_gb outfile
#bug report: joey0576@163.com
#2014-04-11

from Bio import SeqIO
import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


seq_records = []

parentAlignFile = sys.argv[1]
namelistFile = sys.argv[2]
sonAlignFileName=""
if len(sys.argv) < 4:
	sonAlignFileName = "sonAlignmentFile.fasta"
else:
	sonAlignFileName = sys.argv[3]

namelist = {}
namelistFileContent = open(namelistFile)
for line in namelistFileContent:
	namelist[line[0:8]]=line[:-1]

namelistFileContent.close()


alignFile = open(parentAlignFile)


for seqrecord in SeqIO.parse(alignFile,"fasta"):	
	seq_accession = seqrecord.id
	tmp = seq_accession[0:8]
	if namelist.has_key(tmp):
		newseq = SeqRecord(seqrecord.seq,id = namelist[tmp], description="")
		seq_records.append(newseq)

SeqIO.write(seq_records, sonAlignFileName, "fasta")
	
alignFile.close() 
