# building a graph as an adjacency list

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def addEdge(self, v1, v2, cost=0):
        if v1 not in self.vertList:
            nv = self.addVertex(v1)
        if v2 not in self.vertList:
            nv = self.addVertex(v2)
        
        self.vertList[v1].addNeighbor(self.vertList[v2], cost)

    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
    
    def __contains__(self,n):
        return n in self.vertList

g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)
g.addEdge(0,1,2)
g.addEdge(0,2,2)
for v in g:
    print(v)
    print(v.getConnections)
    print()