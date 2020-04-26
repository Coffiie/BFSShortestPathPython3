def bfs(G,s,d):
    visited = []
    queue=[s]
    parent = [0] * len(G)
    while queue:
        node = queue.pop(0)
        if node == d:
            break
        if node not in visited:
            visited.append(node)
            neighbours = G[node]
            for n in neighbours:
                print("node: " + str(node))
                print("neighbor: "+str(n))
                if n not in visited:
                    parent[n] = node
                queue.append(n)
    for i in range(0,len(parent)):
        print("parent "+str(i)+" : "+str(parent[i]))
    return parent

def printShortestPath(parent,s,d):
    print("This is a bi-directional graph so we get bi-directional paths")
    print("I am printing backward Path to source, but it is both ways: ")
    val = d
    while True:
        print(str(val)+"->"+str(parent[val]),end=",")
        val = parent[val]
        if val == s:
            break