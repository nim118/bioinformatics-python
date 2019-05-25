# Problem Url : http://rosalind.info/problems/ddeg/
f = open("double_degree_array.txt", "r")

f_data = f.readlines()

first_line = f_data.pop(0).strip().split(" ")

number_of_vertices = int(first_line[0])
number_of_edges = int(first_line[1])

vertices_neighbors = [0] * number_of_vertices
degree_of_vertex = [0] * number_of_vertices

for line in f_data:
	line = line.split(" ")
	vertex1 = int(line[0])
	vertex2 = int(line[1])
	# vertices_neighbors[vertex1] =
	degree_of_vertex[vertex1 - 1] += 1
	degree_of_vertex[vertex2 - 1] += 1 

for line in f_data:
	line = line.split(" ")
	vertex1 = int(line[0])
	vertex2 = int(line[1])
	vertices_neighbors[vertex1 - 1] += degree_of_vertex[vertex2 - 1]
	vertices_neighbors[vertex2 - 1] += degree_of_vertex[vertex1 - 1] 

print " ".join(str(e) for e in vertices_neighbors)