f = open("connected_components.txt", "r")

f_data = f.readlines()

first_line = f_data.pop(0).strip().split(" ")

number_of_vertices = int(first_line[0])
number_of_edges = int(first_line[1])

#to create array of array for all vertices
vertices = []
for i in range(number_of_vertices):
    vertices.append([])
#to list down adjecent vertices for all vertex
for edge in f_data:
    edge = edge.split(" ")
    vertex1 = int(edge[0])
    vertex2 = int(edge[1])
    vertices[vertex1 - 1].append(vertex2)
    vertices[vertex2 - 1].append(vertex1)

#create and array for all vertex to save visited or not 
visited_vertices = [] 
for j in range(number_of_vertices):
    visited_vertices.append(False)

#dfs 
depth_stack = []
for i in range(number_of_vertices):
    #check if current vertex is already in depth_stack
    # if not push it in depth stack and mark visited
        #lo
    #if Visited go to next vertex