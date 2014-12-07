#!usr/bin/python

import sys
from Bio import SeqIO
import numpy

def trim_adaptors(records, adaptor):

    len_adaptor = len(adaptor) #cache this for later
    for record in records:
        index = record.seq.find(adaptor)
        if index == -1:
            #adaptor not found, so won't trim
            yield record
        else:
            #trim off the adaptor
            yield record[index+len_adaptor:]

def trim_amubiguousN(records):
    for record in records:
        index = record.seq.find("N")
        if index == -1:
            yield record
        else:
            yield record[index:]

def get_quality(records):
    for record in records:
        #print len(record.letter_annotations["phred_quality"])
        tmp = numpy.mean(record.letter_annotations["phred_quality"])
        tmplist.extend(tmp)

infileneme = sys.argv[1]
original_reads = SeqIO.parse(infileneme, "fastq")
##trimmed_reads = trim_adaptors(original_reads, "GATGACGGTGT")
tmplist =[]
get_quality(original_reads)
print min(tmplist)
print max(tmplist)
#trimmed_reads = trim_amubiguousN(original_reads)
#SeqIO.write(trimmed_reads, "trimmed.fastq", "fastq") 
#print("Saved %i reads" % count)
