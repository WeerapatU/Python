##description: this script is write to extract information from genbank file
##              outout file content ",", so use "\t" to separate information item.
#usage: python extractInfo.py infile_gb outfile
#bug report: joey0576@163.com

from Bio import SeqIO
import sys

# if len(sys.argv) < 3:
# 	print "Usage: python extractInfo_v2.py your_genbank_file output_file_name sequence_length_filter"
# 	sys.exit(2)
# else:
	#extract information from gb file

	infile = sys.argv[1]
	outfile = sys.argv[2]

	# if len(sys.argv) == 4:
	# 	lengthFilter = sys.argv[3]

	gbinfile = open(infile)
	seqInfo = ""
	for seqrecord in SeqIO.parse(gbinfile,"genbank"):
		val = ["null"] *14
		(seq_version, seq_accession, seq_seq, seq_desc, seq_source, 
			seq_strain, seq_collectdate, seq_host, seq_isolate,
			seq_country, seq_isolation_source, seq_organism, seq_mol_type, 
			seq_serotype,seq_gi,cds_id,cds_gi, cds_seq, cds_product, translation_len, seq_note) = ["null"] *21
		
		seq_accession = seqrecord.id.split(".")[0]
		seq_version  = seqrecord.id.split(".")[1]   #id ,version
		seq_gi = seqrecord.annotations["gi"]  #gi
		seq_seq = seqrecord.seq   # sequence
		seq_length = len(seqrecord.seq)
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

				if item.qualifiers.has_key("note"):
					seq_note = str(item.qualifiers["note"])[2:-2]

			if item.type == "CDS":
				if item.qualifiers.has_key("protein_id"):
					cds_id = str(item.qualifiers["protein_id"])[2:-2]
				
				if item.qualifiers.has_key("db_xref"):
					cds_gi = (str(item.qualifiers["db_xref"])[2:-2]).split(":")[1]

				if item.qualifiers.has_key("translation"):
					cds_seq = str(item.qualifiers["translation"])[2:-2]
					translation_len = len(cds_seq)

				if item.qualifiers.has_key("product"):
					cds_product = str(item.qualifiers["product"])[2:-2]

		print cds_id
		seqInfo += cds_id + "\n" + translation  +"\n"

	output = open(outfile,"w")
	output.write(seqInfo)

	output.close()
	gbinfile.close() 
