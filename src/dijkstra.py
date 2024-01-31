import random
class Graph:
    # Create adjacency matrix
    def __init__(self, size):
        self.adjMatrix = []
        for _ in range(size):
            self.adjMatrix.append([0 for _ in range(size)])
        self.size = size
        self.nodeSet = set(i for i in range(size)) # Indices of nodes

    # Add edge to matrix
    def add_edge(self, n1, n2):
        if n1==n2:
            print(f"Same vertex {n1} and {n2}.")
            return
        self.adjMatrix[n1][n2]=1
        self.adjMatrix[n2][n1]=1
    
    # Remove edge from matrix
    def remove_edge(self, n1, n2):
        if self.adjMatrix[n1][n2]==0:
            print(f"No edge between {n1} and {n2}.")
            return
        self.adjMatrix[n1][n2] = 0
        self.adjMatrix[n2][n1] = 0
        
    def __len__(self):
        return self.size
    
    # Print matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val), end="")
            print("\n")
            
class diGraph(Graph): # Subclass for directed graphs
    def add_edge(self, n1, n2):
        self.adjMatrix[n1][n2] = 1
        
    def remove_edge(self, n1, n2):
        self.adjMatrix[n1][n2] = 0
        
class wdiGraph(diGraph): # Subclass for directed and weighted graphs
    def add_edge(self, n1, n2, length):
        self.adjMatrix[n1][n2] = length
        
    def remove_edge(self, n1, n2):
        self.adjMatrix[n1][n2] = 0
        
    def edge_length(self, n1, n2):
        return self.adjMatrix[n1][n2]


def findNextNode(graph, S, spDistances): # S is explored nodes, spDistances is a list of shortest path distances from start node.
    unexploredNodes = graph.nodeSet.difference(S)
    
    minDist = 1e7 # Set distances to a large number
    nextNode = random.choice(list(unexploredNodes))
    
    for newNode in unexploredNodes:
        for oldNode in S:
            if graph.edge_length(oldNode, newNode) != 0:
                dist = spDistances[oldNode] + graph.edge_length(oldNode, newNode)
                if (dist < minDist):
                    nextNode = newNode
                    minDist = dist
    
    return nextNode, minDist

def dijkstra(graph, start_node):
    S = set()
    S.add(start_node)
    
    spDistances = ["U" for _ in range(graph.size)]
    spDistances[start_node] = 0
    
    while S!=graph.nodeSet:
        nextNode, nextNodeDist = findNextNode(graph, S, spDistances)
        
        S.add(nextNode)
        spDistances[nextNode] = nextNodeDist
        
    return spDistances
                
def main():
    myGraph = wdiGraph(6)
    myGraph.add_edge(0,1,1)
    myGraph.add_edge(0,2,2)
    myGraph.add_edge(0,3,4)
    myGraph.add_edge(1,4,3)
    myGraph.add_edge(1,3,1)
    myGraph.add_edge(2,5,3)
    myGraph.add_edge(2,3,2)
    myGraph.add_edge(3,5,2)
    myGraph.add_edge(3,4,1)

    shortestDistances=dijkstra(myGraph, 0)
    print(shortestDistances)

if __name__ == "__main__":
    main()