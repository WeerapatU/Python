#计算一个序列数据集（fasta格式）中每条序列的GC含量，输出格式“序列ID，GC含量”的csv格式文件
#2013-12-19

from Bio.Seq import Seq
from Bio.Seq import GC
from Bio.Seq import SeqIO
import sys

infilename=sys.argv[1]
output=""
seqfile = open(infilename,"rU")
for seqRecord in SeqIO.parse(seqfile,"fasta"):
	GCcount=GC(seqRecord.seq)
	output += seqRecord.id + "," + GCcount + "\t"


outfile = open("result-GCcount.csv","w")
outfile.write(output)

seqfile.close()
outfile.close()
