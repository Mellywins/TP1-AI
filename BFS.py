# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
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

    # Function to print a BFS of graph
    def BFS(self, s, search=0):

        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # exit if search item is found
            if search and search == s:
                exit()

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


# Driver code


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

print("Breadth First")
g.BFS(2)
print("")
g.BFS(2, 5)

# This code is contributed by Neelam Yadav
