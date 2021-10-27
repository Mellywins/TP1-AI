# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation


class Graph:

    # Constructor
    def __init__(self, graph=None):
        if graph is None:
            # default dictionary to store graph
            self.graph = defaultdict(list)
        else:
            self.graph = graph

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited, search,counter=1):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')
        # Exit if search item is found
        if search and search == v:
            print('visited nodes: ', len(visited))
            exit()


        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            counter+=1
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited, search,counter)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v, search=0):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        return self.DFSUtil(v, visited, search)




graph_elements = {0: [1, 2],
                  1: [2, 5],
                  2: [0, 3],
                  3: [4, 3],
                  4: [0],
                  5: [2],
                  }

# Create a graph given in the above diagram
g = Graph(graph_elements)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(1, 5)
# g.addEdge(5, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 4)
# g.addEdge(3, 3)
# g.addEdge(4, 0)

print("Depth First")
# g.DFS(2)
print("")
x=g.DFS(2, 3)
