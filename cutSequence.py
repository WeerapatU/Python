##description: 
#usage: 
#bug report: joey0576@163.com
#2014-04-16

from Bio import SeqIO
import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


vp1_seq_records = []
vp2_seq_records = []
vp3_seq_records = []
vp4_seq_records = []
p2a_seq_records = []
p2b_seq_records = []
p2c_seq_records = []
p3a_seq_records = []
p3b_seq_records = []
p3c_seq_records = []
p3d_seq_records = []

inAlignFile = sys.argv[1]

alignFile = open(inAlignFile)

for seqrecord in SeqIO.parse(alignFile,"fasta"):
	vp1_seq_records.append(SeqRecord(seqrecord.seq[1695:2585],id = seqrecord.id, description=""))
	# vp2_seq_records.append(SeqRecord(seqrecord.seq[207:968],id = seqrecord.id, description=""))
	# vp3_seq_records.append(SeqRecord(seqrecord.seq[969:1694],id = seqrecord.id, description=""))
	# vp4_seq_records.append(SeqRecord(seqrecord.seq[0:206],id = seqrecord.id, description=""))
	# p2a_seq_records.append(SeqRecord(seqrecord.seq[2586:3535],id = seqrecord.id, description=""))
	# p2b_seq_records.append(SeqRecord(seqrecord.seq[3536:],id = seqrecord.id, description=""))
	# p2c_seq_records = []
	# p3a_seq_records = []
	# p3b_seq_records = []
	# p3c_seq_records = []
	# p3d_seq_records = []	
	# utr3_seq_records.append(SeqRecord(seqrecord.seq[0:753],id = seqrecord.id, description=""))
	# utr5_seq_records.append(SeqRecord(seqrecord.seq[7337:],id = seqrecord.id, description=""))

SeqIO.write(vp1_seq_records, "91genomes_aligned_vp1.fasta", "fasta")

#SeqIO.write(utr3_seq_records, "91genomes_aligned_3utr.fasta", "fasta")

alignFile.close() 
