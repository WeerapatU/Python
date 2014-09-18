##description: 
#usage: python namereplace.py infile_gb outfile
#bug report: joey0576@163.com

from Bio import SeqIO
import sys
import re
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna

print """			
			*******usage*****      
 		Usage: python namereplace.py infile_gb outfile 
		output sequqnce id : 'accession number'_'strain' 
		write sequences to file sequence_out.fasta
		done.
			*****************       """

seq_records = []

infile = sys.argv[1]
#outfile = sys.argv[2]

gbinfile = open(infile)
seqInfo = "accession"+"\t"+"gi" +"\t"+ "strain" + "\t" + "country" +"\t"+"collection_date"

for seqrecord in SeqIO.parse(gbinfile,"genbank"):
	seq_defi = seqrecord.description
	seq_seq = seqrecord.seq   # sequence
	seq_desc = seqrecord.description #sequence description
	
	seq_strain = seq_defi.split(" ")[2] + "-" + seq_defi.split(" ")[3][0:3] + "-" + seq_defi.split(" ")[4][:-1]
	
	newseq = SeqRecord(seq_seq,id = seqrecord.id +"_"+seq_strain, description="")
	seq_records.append(newseq)

SeqIO.write(seq_records, "sequence_out.fasta", "fasta")
	
gbinfile.close() 
