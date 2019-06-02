# http://rosalind.info/problems/cc/
# code to print connected components in a graph
class Graph:

    #Init function to declare class variables 
    def __init__(self, V):
        self.V   = V
        self.adj = [[] for i in range(V)]
    
    #Function to add edge in the graph
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    #Function to retrieve connected components 
    def getConnectedComponents(self):
        visited = []
        cc      = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc
    
    #Function for DFS of graph
    def DFSUtil(self, temp, v, visited):
        #mark the current vertex as visited.
        visited[v] = True

        #store the vertex to the list , doing + 1 to remove 
        # manage the difference between array index from 0 and vertex starting from 1 
        temp.append(v + 1)

        #repeat for all the vertices adjacent to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
                #update the list 
                temp = self.DFSUtil(temp, i, visited)

        return temp

#Driver Code.
if __name__ == "__main__":

    # Code to read data from the file
    f = open("connected_components.txt", "r")
    

    f_data             = f.readlines()
    first_line         = f_data.pop(0).strip().split(" ")
    number_of_vertices = int(first_line[0])
    number_of_edges    = int(first_line[1])

    #Create a graph given in the input
    g = Graph(number_of_vertices);
    
    for edge in f_data:
        edge = edge.split(" ")
        vertex1 = int(edge[0])
        vertex2 = int(edge[1])
        #Doing minus 1 as array is starting from 0 and vertices are from 1
        g.addEdge(vertex1-1, vertex2-1)

    cc = g.getConnectedComponents()

    #print(cc)
    print(len(cc))
