#!/user/bin/python

#2014-10-31
# process orf fasta sequences to get sequences of  ribosome binding site

import sys
from Bio import SeqIO

infilename = sys.argv[1]
infile = open(infilename, "r")

outfilename = sys.argv[2]

new_content = ""

for record in SeqIO.parse(infile, "fasta"):
	desc_features = record.description.split("SGDID:")
	sgdid = desc_features[1].split(",")[0]
	chr_name_position = (desc_features[1].split(",")[1]).split(" ")
	chr_name = chr_name_position[2]
	chr_position = chr_name_position[4]

	seq_id = sgdid+"_"+chr_name+"_"+chr_position
	#print seq_id
	new_content += ">" + seq_id + "\n" + record.seq+"\n"

output = open(outfilename, "w")
output.write(str(new_content))
output.close()

infile.close()