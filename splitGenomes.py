#2014-01-18
from Bio import SeqIO
import sys
from Bio.SeqRecord import SeqRecord

def writeFile(output, filename):
	outfile = open(filename,"w")
	outfile.write(str(output))
	outfile.close()

(seqsRecords_5utr, seqsRecords_vp4, seqsRecords_vp2,seqsRecords_vp3,seqsRecords_vp1 )= [[]]*5
(seqsRecords_2a,seqsRecords_2b,seqsRecords_2c,seqsRecords_3a,seqsRecords_3b) = [[]]*5
(seqsRecords_3c,seqsRecords_3d, seqsRecords_3utr,seqsRecords_cds) = [[]]*4

fastaFile = open(sys.argv[1])
(output_5UTR,output_VP4, output_VP3, output_VP2,output_VP1, output_2A, output_2B, output_2C, output_3A, output_3B, output_3C ,output_3D,output_3UTR,output_cds)=[""]*14

for record in SeqIO.parse(fastaFile,"fasta"):
	#print record.id
	seq = record.seq
	output_5UTR += ">" +record.id+"\n" +seq[:756] +"\n"  #

	#output_5UTR = seq[:1884]
	new = SeqRecord(str(output_5UTR), id = record.id, description="")
	#print new
	seqsRecords_5utr.append(new)
	#seqsRecords_5utr.append(SeqRecord(str(output_5UTR), id = record.id, description=""))

	output_VP4 += ">" +record.id+"\n" + seq[757:960]+"\n" #
	#print len(seq[1882:2085])
	output_VP2 += ">" +record.id+"\n" + seq[961:1726]+"\n" #
	#print  len(seq[2086:2851])
	output_VP3 += ">" +record.id+"\n" + seq[1727:2453]+"\n" #
	#print len(seq[2852:3578])
	output_VP1 += ">" +record.id+"\n" + seq[2454:3345]+"\n"#
	#print len(seq[3579:4470])
	output_2A += ">" +record.id+"\n" + seq[3346:3796]+"\n" #
	#print len(seq[4471:4921])
	output_2B += ">" +record.id+"\n" + seq[3797:4095]+"\n" #
	#print len(seq[4922:5219])
	output_2C += ">" +record.id+"\n" + seq[4096:5083]+"\n" #
	#print len(seq[5220:6207])
	output_3A += ">" +record.id+"\n" + seq[5084:5343]+"\n" #
	#print len(seq[6208:6466])
	output_3B += ">" +record.id+"\n" + seq[5344:5410]+"\n" #
	#print  len(seq[6467:6533])
	output_3C += ">" +record.id+"\n" + seq[5411:5960]+"\n"
	#print len(seq[6534:7083])
	output_3D += ">" +record.id+"\n" + seq[5961:7347]+"\n"
	#print len(seq[7084:8480])
	output_3UTR += ">" +record.id+"\n" +seq[7348:]+"\n"
	output_cds += ">"+record.id +"\n"+seq[757:7338] + "\n"
	#print len(seq)
	#print  len(seq[:1881]) + len(seq[1882:2085])+ len(seq[2086:2851])+ len(seq[2852:3578])+ len(seq[3579:4470])+ len(seq[4471:4921])+ len(seq[4922:5219])+ len(seq[5220:6207])+ len(seq[6208:6466])+ len(seq[6467:6533])+ len(seq[6534:7083])+ len(seq[7084:8480])+ len(seq[8481:])
	# print "vp4: "+len(output_VP4)
	# print len(output_VP2)
	# print len(output_VP2)
# 
# writeFile(output_5UTR, "172genomes_5utr.fasta")
# writeFile(output_VP4, "172genomes_vp4.fasta")
# writeFile(output_VP2, "172genomes_vp2.fasta")
# writeFile(output_VP3, "172genomes_vp3.fasta")
# writeFile(output_VP1, "172genomes_vp1.fasta")
# writeFile(output_2A, "172genomes_2a.fasta")
# writeFile(output_2B, "172genomes_2b.fasta")
# writeFile(output_2C, "172genomes_2c.fasta")
# writeFile(output_3A, "172genomes_3a.fasta")
# writeFile(output_3B, "172genomes_3b.fasta")
# writeFile(output_3C, "172genomes_3c.fasta")
# writeFile(output_3D, "172genomes_3d.fasta")
# writeFile(output_3UTR, "172genomes_3utr.fasta")

writeFile(output_cds, "172genomes_cds.fasta")
#print seqsRecords_5utr

fastaFile.close()


	
	# seqsRecords_vp4.append(SeqRecord(output_VP4, id = record.id, description=""))
	# seqsRecords_vp2.append(SeqRecord(output_VP2, id = record.id, description=""))
	# seqsRecords_vp3.append(SeqRecord(output_VP3, id = record.id, description=""))
	# seqsRecords_vp1.append(SeqRecord(output_VP1, id = record.id, description=""))
	# seqsRecords_2a.append(SeqRecord(output_2A, id = record.id, description=""))
	# seqsRecords_2b.append(SeqRecord(output_2B, id = record.id, description=""))
	# seqsRecords_2c.append(SeqRecord(output_2C, id = record.id, description=""))
	# seqsRecords_3a.append(SeqRecord(output_3A, id = record.id, description=""))
	# seqsRecords_3b.append(SeqRecord(output_3B, id = record.id, description=""))
	# seqsRecords_3c.append(SeqRecord(output_3C, id = record.id, description=""))
	# seqsRecords_3d.append(SeqRecord(output_3D, id = record.id, description=""))
	# seqsRecords_3utr.append(SeqRecord(output_3UTR, id = record.id, description=""))


	#SeqIO.write(seqsRecords_5utr, "172genomes_5utr.fasta", "fasta")
# SeqIO.write(seqsRecords_vp4, "172genomes_vp4.fasta", "fasta")
# SeqIO.write(seqsRecords_vp2, "172genomes_vp2.fasta", "fasta")
# SeqIO.write(seqsRecords_vp3, "172genomes_vp3.fasta", "fasta")
# SeqIO.write(seqsRecords_vp1, "172genomes_vp1.fasta", "fasta")
# SeqIO.write(seqsRecords_2a, "172genomes_2a.fasta", "fasta")
# SeqIO.write(seqsRecords_2b, "172genomes_2b.fasta", "fasta")
# SeqIO.write(seqsRecords_2c, "172genomes_2c.fasta", "fasta")
# SeqIO.write(seqsRecords_3a, "172genomes_3a.fasta", "fasta")
# SeqIO.write(seqsRecords_3b, "172genomes_3b.fasta", "fasta")
# SeqIO.write(seqsRecords_3c, "172genomes_3c.fasta", "fasta")
# SeqIO.write(seqsRecords_3d, "172genomes_3d.fasta", "fasta")
# SeqIO.write(seqsRecords_3utr, "172genomes_3utr.fasta", "fasta")