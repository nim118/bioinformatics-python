f = open("rosalind_deg (1).txt", "r")
#f = open("degree_array_input.txt", "r")

f_data = f.readlines()

first_line = f_data[0].strip()
first_line = first_line.split( " ")

number_of_vertices = int(first_line[0])
number_of_edges = int(first_line[1])

#print number_of_vertices
#print number_of_edges

#exit()

del f_data[0]
degree_data = [0] * number_of_vertices

#print degree_data
#exit()

for line in f_data:
	line = line.split(" ")
	vertex1 = int(line[0])
	vertex2 = int(line[1])

	degree_data[vertex1 - 1] = degree_data[vertex1 - 1] + 1
	degree_data[vertex2 - 1] = degree_data[vertex2 - 1] + 1

#del degree_data[0]

degree_data_string = " ".join(str(e) for e in degree_data)

print degree_data_string