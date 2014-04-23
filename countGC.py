#count GC of every sequence from dataset(fasta format)
#output format: "seqeunce_Id,GCcount" in csv format
#2013-12-19

from Bio.Seq import Seq
from Bio.SeqUtils import GC
from Bio import SeqIO
import sys

infilename=sys.argv[1]
output=""
seqfile = open(infilename,"rU")
for seqRecord in SeqIO.parse(seqfile,"fasta"):
	GCcount=GC(seqRecord.seq)
	output += seqRecord.id + "," + str(GCcount) + "\n"


outfile = open("result-GCcount.csv","w")
outfile.write(output)

seqfile.close()
outfile.close()
