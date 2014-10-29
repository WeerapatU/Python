#!/user/bin/python/

## description: map orf to S.cerevisiae S288c reference genome.
##todo: to simplify the code

import csv
import sys


in_file = sys.argv[1]
csv_file = open(in_file,"r")

csv_content = csv.reader(csv_file, delimiter=",")

y = 0.01

chrosome_name = ["chr I","chr II","chr III","chr IV" ,"chr V","chr VI","chr VII","chr VIII","chr IX","chr X","chr XI","chr XII","chr XIII","chr XIV","chr XV","chr XVI","mit complet"]
chrosome_length = [230218,813184,316620,1531933,576874,270161,1090940,562643,439888,745751,666816,1078177,924431,784333,1091291,948066,85779]


# ### version 1.0 --- map orf to whole genome(S288c)
# coordinate_orf = ""

# for row in csv_content:
# 	for i in (range(0,len(chrosome_name))):
# 		if chrosome_name[i] in row[1]:
# 			tmp_add = 0
# 			if i ==0:
# 				coordinate_orf += str(row[3]) + ","+ str(y) + ","+ str(row[2])+ "\n"
# 				coordinate_orf += str(row[4]) + "," +str(y) + ","+ str(row[2])+ "\n"

# 			#coordinate_orf += str(row[3])
# 			else:
# 				tmp_add += chrosome_length[i]
# 				coordinate_orf += str(int(row[3]) + tmp_add) + "," + str(y) + ","+ str(row[2])+ "\n"
# 				coordinate_orf += str(int(row[4]) + tmp_add) + "," + str(y) + "," +str(row[2])+"\n"
				


# 	# if "chr I" in row[1]:
# 	# 	coordinate_orf += str(row[3]) + "," +str(y) + "\n"
# 	# 	coordinate_orf += str(row[4]) + "," +str(y) + "\n"
	
# 	# else:
# 	# 	print "not chrsome I"230218

# 	# coordinate_orf += str(row[3]) + "," +str(y) + "\n"
# 	# coordinate_orf += str(row[4]) + "," +str(y) + "\n"
# 		y+= 0.01
# output = open("Coordinates_in_orfs_map.csv","w")
# output.write(str(coordinate_orf))

# output.close()

### version 2.0 --- map orfs to chromosome
coordinate_orf = ""

for row in csv_content:
	for i in (range(0, len(chrosome_name))):
		if chrosome_name[i] == row[1]:
			coordinate_orf += str(row[3]) + ","+ str(y) + ","+ str(row[2])+ "\n"
			coordinate_orf += str(row[4]) + "," +str(y) + ","+ str(row[2])+ "\n" 
			y +=0.01
		else:
			y= 0.01
	out_file_name = "./chromosome/" + row[1] + "_orfs_position.csv"
	output = open(out_file_name, "a")
	output.write(str(coordinate_orf))
	output.close()
	coordinate_orf = ""




csv_file.close()



