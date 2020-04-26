from Graph import Graph
import bfs
numberOfVertices = 12
numberOfVertices = numberOfVertices + 1
graph = Graph(numberOfVertices)
graph.addNeighbor(1,2)
graph.addNeighbor(1,7)
graph.addNeighbor(1,8)
graph.addNeighbor(2,1)
graph.addNeighbor(2,3)
graph.addNeighbor(2,6)
graph.addNeighbor(3,2)
graph.addNeighbor(3,4)
graph.addNeighbor(3,5)
graph.addNeighbor(4,3)
graph.addNeighbor(5,3)
graph.addNeighbor(6,2)
graph.addNeighbor(7,1)
graph.addNeighbor(8,1)
graph.addNeighbor(8,12)
graph.addNeighbor(8,9)
graph.addNeighbor(9,10)
graph.addNeighbor(9,8)
graph.addNeighbor(9,11)
graph.addNeighbor(10,9)
graph.addNeighbor(11,9)
graph.addNeighbor(12,8)
graph.printAdjacencyList()
source = 11
destination = 4
parent = dfs.bfs(graph.adjacencyList,source,destination)
dfs.printShortestPath(parent,source,destination)
