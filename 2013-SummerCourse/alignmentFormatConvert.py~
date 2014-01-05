##
##usage: python akignmentformatconvert.py infilename infiletype outfilename outfiletype
##bug report:joey0576@163.com

from Bio import AlignIO
import sys

if len(sys.argv) != 5:
	print "Usage: python akignmentformatconvert.py infilename infiletype outfilename outfiletype"
	sys.exit(2)
else:
	infile = sys.argv[1]
	outfile = sys.argv[3]
	intype = sys.argv[2]
	outtype = sys.argv[4]
	formatlist=["fasta","phylip","stockholm", "clustal"]
	if intype not in formatlist or outtype not in formatlist:
		print "wrong formatlist,check infile type and outfile type!"
		print "accepted format:fasta,phylip,stockholm,clustal"
		sys.exit(2)
	else:
		alignmentin = AlignIO.parse(infile,intype)
		alignmentout = AlignIO.write(alignmentin,outfile,outtype)



# print infile , intype, outfile, outtype

##three ways to convert alignment format
#method 1
# alignmentin = AlignIO.parse(infile, intype)
# alignmentout = AlignIO.write(alignmentin, outfile, outtype)

#method 2
# from Bio import AlignIO
# alignment = AlignIO.convert("vp1.fasta", "fasta", "vp1.phy", "phylip")
# print  "converted alignments" + "\n" + alignment

#method 3
# from Bio import AlignIO
# alignment_in = AlignIO.parse("vp1.fasta", "fasta")
# alignment_out = AlignIO.write(alignment_in, "vp1.phy", "phylip")
# print  "coverted alignments" + "\n" + alignment_out
