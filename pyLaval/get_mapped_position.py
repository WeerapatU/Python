#!user/bin/python

##line in sam files

# SRR1258539.6
# 16	
# chrXII	
# 461824	
# 255	
# 14S37M	
# *	
# 0	
# 0	
# GATGGTGCCTACAGGGTAGTGGTATTTCACTGGCGCCGAAGCTCCCACTTA	
# HIIHHDFGIIGIGIFBBD?GAHJIIIFHFHHGEIIHIGHFFHFFEDBD@@?	
# AS:i:74	
# XN:i:0	
# XM:i:0	
# XO:i:0	
# XG:i:0	
# NM:i:0	
# MD:Z:37	
# YT:Z:UU

##lines in csv file
#sORF-19,XLOC_003307+,chrXV:38888-39046,N/A,100,3.00E-26,105,N.D.,33.96,0.005,37,N.S.,0,-,-,-,0,-,-,-,0,-,-,-,0,-,-,-,0,-,-,-,0,-,-,-,0,-,-,-



import sys
import csv



def get_position_from_sam(infile):
	all_mapped_content = ""
	for line in infile:
		## strand	chrosomename	start_position sequence seq_len
		## [1]		[2]				[3]				[9]		len([9])
		line_group = line.split("\t")
		
		if line_group[2].startswith("chr"):
			tmp = line_group[1]+","+line_group[2]+","+line_group[3]+","+line_group[9]+","+str(len(line_group[9]))+"\n"
			all_mapped_content += tmp
		#print len(line.split("\t"))

	return all_mapped_content

def combine_to_orf(mapped_reads, orf_list):
	for line in mapped_reads:
		line_group = line.split(",")
		for i in range(len(orf_list)):
			#orf_list[i]
		#for item in orf_list: 
			if line_group[1] in orf_list[i]:
				chro_mapped = line_group[1]
				chro_orf = orf_list[i][0]
				
				strand_mapped = line_group[0]
				strand_orf = orf_list[i][1]

				start_mapped = line_group[2]
				start_orf = orf_list[i][2]
				end_orf = orf_list[i][3]
				len_mapped = line_group[4]
				
				##both in +1 strand
				if strand_mapped == "16" and "F" in strand_orf:
					# print start_mapped
					# print start_orf
					# print start_mapped
					# print end_orf
					#orf_list[i][4] = 558
					#print "hello1"
					#print orf_list[i][4]
					if start_mapped >= start_orf and start_mapped <= end_orf:
						#print "hello2"
						distance_in_mapped_orf = (end_orf - start_mapped)
						if distance_in_mapped_orf >= len_mapped:
							orf_list[i][4] += len_mapped
							#print orf_list[i][4] 
						else :
							orf_list[i][4] +=  distance_in_mapped_orf
							#print orf_list[i][4] 

				## mapped in +1 strand, orf in -1 strand 
				elif strand_mapped == "16" and "R" in strand_orf:
					if start_mapped >= end_orf and start_mapped <= start_orf:
						distance_in_mapped_orf = start_orf - strand_mapped
						if distance_in_mapped_orf >= len_mapped:
							orf_list[i][4] += len_mapped
							#print orf_list[i][4] 
						else:
							orf_list[i][4] += distance_in_mapped_orf
							#print orf_list[i][4] 

				##mapped in -1 strand, and orf in +1 strand
				elif strand_mapped == "0" and "F" in strand_orf:
					if start_mapped <= end_orf and strand_mapped >= start_orf:
						distance_in_mapped_orf = strand_mapped - start_orf 
						if distance_in_mapped_orf >=len_mapped:
							orf_list[i][4] += len_mapped
							#print orf_list[i][4] 
						else:
							orf_list[i][4] += distance_in_mapped_orf
							#print orf_list[i][4] 
				##both in _1 strand
				elif strand_mapped == "0" and "R" in strand_orf:
					if start_mapped >= end_orf and start_mapped <= start_orf:
						distance_in_mapped_orf = start_mapped - end_orf
						if distance_in_mapped_orf >= len_mapped:
							orf_list[i][4] += len_mapped
							#print orf_list[i][4] 
						else:
							orf_list[i][4] += distance_in_mapped_orf
							#print orf_list[i][4] 
				else:
					print "no hits"

			print orf_list[i][4]
	return orf_list
			

def orf_info_list(orf_infile):
	orf_list = []
	for line in orf_infile:
		line_group = line.split(",")
		chroso_name, position= line_group[2].split(":")
		start_p , end_p = position.split("-")
		if start_p < end_p:
			tmp_list = [chroso_name,"F", start_p, end_p, 0,line_group[0]]
			orf_list.append(tmp_list)
		else:
			tmp_list = [chroso_name,"R", start_p, end_p, 0,line_group[0]]
			orf_list.append(tmp_list)
		
	return orf_list

#write file out
def write_out(filename, filecontent):
	output = open(filename, "w")
	output.write(filecontent)
	output.close()

def list_to_string(list_list):
	content_list = ""
	for item in list_list:
		for i in item:
			content_list += str(i) +"\t"
		content_list += "\n"
	return content_list

##============== main program ==========
##process 
# infilename = sys.argv[1]
# infile = open(infilename,"r")
# sam_position = get_position_from_sam(infile)
# write_out("mapped_info.csv", sam_position)
# infile.close()

##find position
orf_list = orf_info_list(open(sys.argv[1]))
orf_list1 =  combine_to_orf(open(sys.argv[2]), orf_list)
write_out("mapped_orf_position.csv", list_to_string(orf_list1))


