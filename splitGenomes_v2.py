#deacription: python splitGenomes_v2.py genomes_in_fasta gene_position_csv
#2014-01-18
from Bio import SeqIO
import sys
import csv
from Bio.SeqRecord import SeqRecord

def writeFile(output, filename):
	outputfile = open(filename,"w")
	outputfile.write(output)
	outputfile.close()

(seqsRecords_5utr, seqsRecords_vp4, seqsRecords_vp2,seqsRecords_vp3,seqsRecords_vp1 )= [[]]*5
(seqsRecords_2a,seqsRecords_2b,seqsRecords_2c,seqsRecords_3a,seqsRecords_3b) = [[]]*5
(seqsRecords_3c,seqsRecords_3d, seqsRecords_3utr) = [[]]*3

fastaFile = open(sys.argv[1],"r")
for record in SeqIO.parse(fastaFile,"fasta"):
	print record.id
	seq = record.seq

	output_5UTR = seq[:745]
	#print ("output_5UTR: " +str(len(output_5UTR)))
	output_VP4 = seq[745:948]
	#print ("output_VP4: " +str(len(output_VP4)))
	output_VP2 = seq[948:1713]
	#print ("output_VP2: " +str(len(output_VP2)))
	output_VP3 = seq[1713:2439]
	#print ("output_VP3: " +str(len(output_VP3)))
	output_VP1 = seq[2439:3330]
	#print ("output_VP1: " +str(len(output_VP1)))
	output_2A = seq[3330:3780]
	#print ("output_2A: " +str(len(output_2A)))
	output_2B = seq[3780:4077]
	#print ("output_2B: " +str(len(output_2B)))
	output_2C = seq[4077:5064]
	#print ("output_2C: " +str(len(output_2C)))
	output_3A = seq[5064:5322]
	#print ("output_3A: " +str(len(output_3A)))
	output_3B = seq[5322:5388]
	#print ("output_3B: " +str(len(output_3B)))
	output_3C = seq[5388:5937]
	#print ("output_3C: " +str(len(output_3C)))
	output_3D = seq[5937:7323]
	#print ("output_3D: " +str(len(output_3D)))
	output_3UTR = seq[7323:]
	#print ("output_3UTR: " +str(len(output_3UTR)))

	seqsRecords_5utr.append(SeqRecord(output_5UTR, id = record.id, description=""))
	seqsRecords_vp4.append(SeqRecord(output_VP4, id = record.id, description=""))
	seqsRecords_vp2.append(SeqRecord(output_VP2, id = record.id, description=""))
	seqsRecords_vp3.append(SeqRecord(output_VP3, id = record.id, description=""))
	seqsRecords_vp1.append(SeqRecord(output_VP1, id = record.id, description=""))
	seqsRecords_2a.append(SeqRecord(output_2A, id = record.id, description=""))
	seqsRecords_2b.append(SeqRecord(output_2B, id = record.id, description=""))
	seqsRecords_2c.append(SeqRecord(output_2C, id = record.id, description=""))
	seqsRecords_3a.append(SeqRecord(output_3A, id = record.id, description=""))
	seqsRecords_3b.append(SeqRecord(output_3B, id = record.id, description=""))
	seqsRecords_3c.append(SeqRecord(output_3C, id = record.id, description=""))
	seqsRecords_3d.append(SeqRecord(output_3D, id = record.id, description=""))
	seqsRecords_3utr.append(SeqRecord(output_3UTR, id = record.id, description=""))

	# seqsRecords_5utr.append(SeqRecord(output_5UTR, id = "5UTR", description=""))
	# seqsRecords_vp4.append(SeqRecord(output_VP4, id = "VP4", description=""))
	# seqsRecords_vp2.append(SeqRecord(output_VP2, id = "VP2", description=""))
	# seqsRecords_vp3.append(SeqRecord(output_VP3, id = "VP3", description=""))
	# seqsRecords_vp1.append(SeqRecord(output_VP1, id = "VP1", description=""))
	# seqsRecords_2a.append(SeqRecord(output_2A, id = "2A", description=""))
	# seqsRecords_2b.append(SeqRecord(output_2B, id = "2B", description=""))
	# seqsRecords_2c.append(SeqRecord(output_2C, id = "2C", description=""))
	# seqsRecords_3a.append(SeqRecord(output_3A, id = "3A", description=""))
	# seqsRecords_3b.append(SeqRecord(output_3B, id = "3B", description=""))
	# seqsRecords_3c.append(SeqRecord(output_3C, id = "3C", description=""))
	# seqsRecords_3d.append(SeqRecord(output_3D, id = "3D", description=""))
	# seqsRecords_3utr.append(SeqRecord(output_3UTR, id = "3UTR", description=""))
	
	#seqsRecords.append(newseq)

	# writeFile(">5UTR" +"\n"+str(output_5UTR), "5UTR.fasta")
	# writeFile(">VP4" +"\n"+str(output_VP4), "VP4.fasta")
	# writeFile(">VP2" +"\n"+str(output_VP2), "VP2.fasta")
	# writeFile(">VP3" +"\n"+str(output_VP3), "VP3.fasta")
	# writeFile(">VP1" +"\n"+str(output_VP1), "VP1.fasta")
	# writeFile(">2A" +"\n"+str(output_2A), "2A.fasta")
	# writeFile(">2B" +"\n"+str(output_2B), "2B.fasta")
	# writeFile(">2C" +"\n"+str(output_2C), "2C.fasta")
	# writeFile(">3A" +"\n"+str(output_3A), "3A.fasta")
	# writeFile(">3B" +"\n"+str(output_3B), "3B.fasta")
	# writeFile(">3C" +"\n"+str(output_3C), "3C.fasta")
	# writeFile(">3D" +"\n"+str(output_3D), "3D.fasta")
	# writeFile(">3UTR" +"\n"+str(output_3UTR), "3UTR.fasta")

SeqIO.write(seqsRecords_5utr, "172genomes_5utr.fasta", "fasta")
SeqIO.write(seqsRecords_vp4, "172genomes_vp4.fasta", "fasta")
SeqIO.write(seqsRecords_vp2, "172genomes_vp2.fasta", "fasta")
SeqIO.write(seqsRecords_vp3, "172genomes_vp3.fasta", "fasta")
SeqIO.write(seqsRecords_vp1, "172genomes_vp1.fasta", "fasta")
SeqIO.write(seqsRecords_2a, "172genomes_2a.fasta", "fasta")
SeqIO.write(seqsRecords_2b, "172genomes_2b.fasta", "fasta")
SeqIO.write(seqsRecords_2c, "172genomes_2c.fasta", "fasta")
SeqIO.write(seqsRecords_3a, "172genomes_3a.fasta", "fasta")
SeqIO.write(seqsRecords_3b, "172genomes_3b.fasta", "fasta")
SeqIO.write(seqsRecords_3c, "172genomes_3c.fasta", "fasta")
SeqIO.write(seqsRecords_3d, "172genomes_3d.fasta", "fasta")
SeqIO.write(seqsRecords_3utr, "172genomes_3utr.fasta", "fasta")
fastaFile.close()


