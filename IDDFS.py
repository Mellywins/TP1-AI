# Python program to print DFS traversal from a given
# given graph
from collections import defaultdict


# This class represents a directed graph using adjacency
# list representation
class Graph:

    def __init__(self, vertices):

        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function to perform a Depth-Limited search
    # from given source 'src'
    def DLS(self, src, target, maxDepth, visitedNodes):
        visitedNodes += 1

        if src == target: return True,visitedNodes
        # If reached the maximum depth, stop recursing.
        if maxDepth < 0: return False,visitedNodes

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            operation=self.DLS(i, target, maxDepth - 1, visitedNodes)
            visitedNodes+=operation[1]
            if operation[0]:
                return True,visitedNodes
        return False,visitedNodes

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self, src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        visitedNodes=0
        for i in range(maxDepth):
            result=self.DLS(src, target, i,visitedNodes)
            print('visited nodes: ', result[1])
            if result[0]:
                return True
        return False


# Create a graph given in the above diagram
g = Graph(6);
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


g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(1, 5)
g.addEdge(5, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(3, 3)
g.addEdge(4, 0)

target = 10;
maxDepth = 2;
src = 2

if g.IDDFS(src, target, maxDepth) == True:
    print("Target is reachable from source " +
          "within max depth")
else:
    print("Target is NOT reachable from source " +
          "within max depth")
