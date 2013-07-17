#description: this script is to extract information from blast output in XML format
#usage: python parseBlastXML.py input_xml_file output_file
#bug report:joey0576@163.com

from Bio.Blast import NCBIXML
import sys

if len(sys.argv) !=3:
	print "Usage:python parseBlastXML.py input_xml_file output_file"
	sys.exit(2)
else:
	#get parameters from commandline 
	xmlfile = sys.argv[1] #as input file name
	xmlinfofile = sys.argv[2] #as output file name

	#open input xml file 
	blastxml = open(xmlfile)

	extractInfo = "accession number"+"\t"+"gi"+"\t"+"version"+"\t"+"length"+"\t"+"description" 
	print "***"+"output format: "+extractInfo+ " ***"
	#for loop iterate ietms in xml file
	for blastRecord in NCBIXML.parse(blastxml):
		for alignment in blastRecord.alignments:
			for hsp in alignment.hsps:
				seqlen =  alignment.length # sequence length
				accession =  alignment.title.split("|")[3][:-2] #accession
				gi = alignment.title.split("|")[1] #gi
				version = alignment.title.split("|")[3] #version
				description =  alignment.title.split("|")[4][1:] #sequence def
				#in sequence description have ",", so here use "\t" to separate items
				info =  accession+"\t"+gi+"\t"+version+"\t"+str(seqlen)+"\t"+description
			
				extractInfo += "\n" + info 

	#write extracted information to output file
	output = open(xmlinfofile,"w")
	output.write(extractInfo)

	#close files
	blastxml.close()
	output.close()
