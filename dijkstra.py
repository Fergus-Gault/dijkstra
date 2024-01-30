
class Graph:
    # Create adjacency matrix
    def __init__(self, size):
        self.adjMatrix = []
        for _ in range(size):
            self.adjMatrix.append([0 for _ in range(size)])
        self.size = size

    # Add edge to matrix
    def add_edge(self, v1, v2):
        if v1==v2:
            print(f"Same vertex {v1} and {v2}.")
            return
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
    
    # Remove edge from matrix
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2]==0:
            print(f"No edge between {v1} and {v2}.")
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0
        
    def __len__(self):
        return self.size
    
    # Print matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val), end="")
            print("\n")
            
                
def main():
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()

if __name__ == "__main__":
    main()