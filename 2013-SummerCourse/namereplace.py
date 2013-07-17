##description: this script is write to extract information from genbank file
##              outout file content ",", so use "\t" to separate information item. 
##              then use the ectrected information to replace sequence id.
##              this script is writed based on the extractInfo.py
##				and this script use accession number and strain as sequence id.
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
	val = ["null"] *14
	(seq_version, seq_accession, seq_seq, seq_desc, seq_source, 
		seq_strain, seq_collectdate, seq_host, seq_isolate,
		seq_country, seq_isolation_source, seq_organism, seq_mol_type, 
		seq_serotype,seq_gi,cds_id,cds_gi, cds_seq) = ["null"] *18
	
	seq_accession = seqrecord.id.split(".")[0]
	seq_version  = seqrecord.id.split(".")[1]   #id ,version
	seq_gi = seqrecord.annotations["gi"]  #gi
	seq_seq = seqrecord.seq   # sequence
	seq_desc = seqrecord.description #sequence description
	#print len(seqrecord.seq)
	for item in seqrecord.features:
		#extract source information
		if item.type == "source":
			if item.qualifiers.has_key("country"):
				seq_country = str(item.qualifiers["country"])[2:-2]

			if item.qualifiers.has_key("strain"):
				seq_strain = str(item.qualifiers["strain"])[2:-2]

			if item.qualifiers.has_key("collection_date"):
				seq_collectdate = str(item.qualifiers
					["collection_date"])[2:-2]

			if item.qualifiers.has_key("host"):
				seq_host = str(item.qualifiers["host"])[2:-2]

			if item.qualifiers.has_key("isolate"):
				seq_isolate = str(item.qualifiers["isolate"])[2:-2]

			if item.qualifiers.has_key("isolation_source"):
				seq_isolation_source = str(item.qualifiers
					["isolation_source"])[2:-2]

			if item.qualifiers.has_key("mol_type"):
				seq_mol_type = str(item.qualifiers["mol_type"])[2:-2]

			if item.qualifiers.has_key("organism"):
				seq_organism = str(item.qualifiers["organism"])[2:-2]

			if item.qualifiers.has_key("serotype"):
				seq_serotype = str(item.qualifiers["serotype"])[2:-2]

		if item.type == "CDS":
			if item.qualifiers.has_key("protein_id"):
				cds_id = str(item.qualifiers["protein_id"])[2:-2]
			
			if item.qualifiers.has_key("db_xref"):
				cds_gi = (str(item.qualifiers["db_xref"])[2:-2]).split(":")[1]

			if item.qualifiers.has_key("translation"):
				cds_seq = str(item.qualifiers["translation"])[2:-2]

	if seq_collectdate != "null":
		pattern = re.compile(r'[0-9]{4}')
		match = pattern.match(seq_collectdate)
		if match:
			if match.group() > 2008:
				newseq = SeqRecord(seq_seq,id = seq_accession+"_"+seq_strain, description="")
				seq_records.append(newseq)

	# newseq = SeqRecord(seq_seq,id = seq_accession+"_"+seq_strain, description="")
	# seq_records.append(newseq)

SeqIO.write(seq_records, "sequence_out.fasta", "fasta")
	
gbinfile.close() 
