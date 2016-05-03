import csv
import sys

# set up the BIMTaxonomy array

taxonomy_array = []

cmdargs = str(sys.argv)

# load in Uniclass2 array from command line

with open(str(sys.argv[1]), 'rb') as csvfile:
  spam = csv.reader(csvfile, delimiter=',', quotechar='\"')
  count = 0
  for row in spam:
	taxonomy_array.append([])
	taxonomy_array[count] = row
	count += 1

# Print opening json bracket
print "["
count = 0
for row in taxonomy_array:

	if (count < len(taxonomy_array)-1):
		print "[\""+taxonomy_array[count][0]+"\",\""+taxonomy_array[count][1]+"\",\""+taxonomy_array[count][2]+"\",\""+taxonomy_array[count][3]+"\"],"
	else:
		print "[\""+taxonomy_array[count][0]+"\",\""+taxonomy_array[count][1]+"\",\""+taxonomy_array[count][2]+"\",\""+taxonomy_array[count][3]+"\"]"

	count +=1

# print closing json bracket

print "]"
