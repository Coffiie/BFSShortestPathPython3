class Graph:
    adjacencyList = []

    def __init__(self,numberOfEdges):
        for i in range(0,numberOfEdges):
            self.adjacencyList.append([])

    def addNeighbor(self,edge,neighbor):
        self.adjacencyList[edge].append(neighbor)

    def printAdjacencyList(self):
        print(self.adjacencyList)
