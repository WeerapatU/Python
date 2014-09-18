#!/usr/bin/python

#the function six_Frame_Translation is modified on http://biopython.org/DIST/docs/api/Bio.SeqUtils-pysrc.html#six_frame_translations
#


from Bio import SeqUtils
from Bio import SeqIO
import sys
import re
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord



def six_Frame_Translation(sequence_string, seq_info, genetic_code_type):
	tmp_info = ""
	for strand, nucleotides in [(+1, sequence_string), (-1, sequence_string.reverse_complement())]:
		for frame in range(3):
			length = 3 * ((record_len-frame) // 3) #Multiple of three
			
			if genetic_code_type == 0:
				## table = 1 ----> The Standard Code
				for pro in nucleotides[frame:frame+length].translate(1).split("*"):
				#if len(pro) >= min_pro_len:
					tmp_info += "\n" + seq_info+ "," + str(strand) + "," + str(frame) + "," + str(len(pro)) +"," + "start not yet" + "," + "end not yet" +"," + pro

			elif genetic_code_type == -1:
			## mitochondrion in yeast
			## table = 2 --->  The Yeast Mitochondrial Code
				for pro in nucleotides[frame:frame+length].translate(2).split("*"):
				#if len(pro) >= min_pro_len: 
					tmp_info += "\n" + seq_info+ "," + str(strand) + "," + str(frame) + "," + str(len(pro)) +"," + "start not yet" + "," + "end not yet" +"," + pro

			
                
				# tmp_info = strand + "," + frame+ "," + len(pro) +"," + "start not yet" + "," \
				# "end mot yet" +"," + pro
			return tmp_info




##main program
in_file = sys.argv[1]
fasta_file = open(in_file)

frame_csv = ""
frame_csv = "Accession,chrosome,strand,frame,length,start_position,end_position,translation"

# seqeuence_file = SeqIO.read(fasta_file,"fasta")
# sequence_count = len(seqeuence_file)

for seqrecord in SeqIO.parse(fasta_file, "fasta"):
	id_pattern = re.compile(r'mit')
	id_match = id_pattern.match(seqrecord.id)
	sequence_string = seqrecord.seq
	record_len = len(seqrecord)
	id_info = seqrecord.id.split("-")[0] +","+ seqrecord.id.split("-")[1] + " " + seqrecord.id.split("-")[2]
	#print type(sequence_string)
	if id_match:
		## mitochondrion in yeast
		genetic_code_type = -1
		frame_csv +=  six_Frame_Translation(sequence_string, id_info, genetic_code_type)
	else:
		## nucul genome
		genetic_code_type = 0
		frame_csv +=  six_Frame_Translation(sequence_string, id_info, genetic_code_type)
	



	##print six_frame_translations(seqrecord.seq)
#print six_frame
# for item in six_frame:
# 	print item
output = open("six grame.csv","w")
output.write(str(frame_csv))

fasta_file.close()
output.close()


