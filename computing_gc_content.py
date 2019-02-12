#reading a file containing data in FASTA format
f = open("fasta_data.txt", 'r')


#reading file data into an array
f_data = f.readlines()



f.close()


print f_data

exit()


#intializing dictionary for data 
dna_strings_gc = {}

count = 0
#converitng FASTA format to dictionary
for dna_string in f_data:
	# print dna_string.strip()
	if (dna_string.strip().find(">") != -1):
		dna_strings_gc[dna_string.strip()[1:]] = f_data[count+1].strip()
	count = count + 1

#initializing dictionary for count
dna_strings_gc_counts = {}
highest = 0
highest_gc_count_dna_string = ""

for dna_string in dna_strings_gc:
	line_total_count = len(dna_strings_gc[dna_string])
	line_gc_count    = 0

	for char in dna_strings_gc[dna_string]:
		#print char
		if (char == 'G') or (char == 'C'):
			line_gc_count = line_gc_count + 1

	print line_gc_count
	print line_total_count
	dna_strings_gc_counts[dna_string] = (float(line_gc_count) / float(line_total_count)) * float(100)

	if (dna_strings_gc_counts[dna_string] > highest):
		highest = dna_strings_gc_counts[dna_string]
		highest_gc_count_dna_string = dna_string



print highest_gc_count_dna_string
print round(highest, 6)
#find the highest number in the dictionary


