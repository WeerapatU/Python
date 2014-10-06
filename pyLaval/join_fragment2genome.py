#join chrosome fragment into whole genome, for genome comparison.
#2014-10-06

import sys
from  Bio  import SeqIO
import collections
from Bio.SeqRecord import SeqRecord

in_file_name = sys.argv[1]

spice_name = (in_file_name.split("_")[0]).split("/")[-1]

out_file_name = "./fragment2genome/" + str(spice_name) + ".genome.fasta"


in_file = open(in_file_name,"r")

id_seq_direct = {}

num_id_direct = {}

whole_genome = ""

for record in SeqIO.parse(in_file,"fasta"):
	index = record.id.split("_")[2]
	num_id_direct[int(index)] = record.id 
	id_seq_direct[record.id] = record.seq 

for item in sorted(num_id_direct):
	#print num_id_direct[item]
	#print id_seq_direct[num_id_direct[item]]
	whole_genome += id_seq_direct[num_id_direct[item]]

#not work at this way
# for key in sorted(id_seq_direct):
# 	print key

#SeqIO.write(SeqRecord(whole_genome, id = spice_name, description = ""), out_file_name,"fasta")

out_file = open(out_file_name,"w")
out_file.write(str(">" + spice_name + "\n" + whole_genome))

out_file.close()
in_file.close()