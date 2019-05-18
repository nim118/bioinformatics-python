#Python program to find connected components
class Graph:
    
    #init function to declare class variables
    def __init__(self,V):
        self.V = V
        self.adj = [[] for i in range(V)]

    