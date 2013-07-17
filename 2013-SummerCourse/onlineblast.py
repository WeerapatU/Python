#bug report: joey0576@163.com

from Bio.Blast import NCBIWWW
from Bio import SeqIO
import sys


#query string to run blast, it can be sequence identifier, sequence itself, or sequence object
querystr = sys.argv[1]
#file name for output file 
outputname = sys.argv[2]

#you can use one of the follow part to run blast

###use sequence identifier as query
blast_result = NCBIWWW.qblast("blastn", "nt", "HM038013")

# ###use sequence string as query
# seqstr=open("HM038013.fasta").read()
# blast_result = NCBIWWW.qblast("blastn", "nt", seqstr)

# ###use sequence itself as query
# seqstr = SeqIO.read(open("HM038013.fasta"),format= "fasta")
# blast_result= NCBIWWW.qblast("blastn", "nt", seqstr.seq) 

# ###use SeqRecord object as query
# seqrecord = SeqIO.read(open("HM038013.fasta"),format = "fasta")
# blast_result = NCBIWWW.qblast("blastn", "nt", seqrecord.format("fasta"))

#save output 
outputfile = open("blast_out.xml","w")
#outputfile = open(outputname,"w")

outputfile.write(blast_result.read())

outputfile.close()
blast_result.close()
