#reading a file containing data in FASTA format
f = open("rosalind_gc (2).txt", 'r')

#reading file data into an array
f_data = f.readlines()

f.close()

#intializing dictionary for data 
dna_strings_gc = {}

index = ''
#converitng FASTA format to dictionary
for dna_string in f_data:
	# print dna_string.strip()
	if (dna_string.strip().find(">") != -1):
		index = dna_string.strip()[1:]
	else :
		if index in dna_strings_gc:
			dna_strings_gc[index] = dna_strings_gc[index] + dna_string.strip()
		else: 
			dna_strings_gc[index] = dna_string.strip()


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


