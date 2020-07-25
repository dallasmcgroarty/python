from collections import OrderedDict 
from enum import Enum

class State(Enum):
    unvisited = 1
    visited = 2
    visiting = 3

class Node:
    def __init__(self, num):
        self.num = num
        self.visitState = State.unvisited
        self.adjacent = OrderedDict() # key = node, value = weight

    def __str__(self):
        return str(self.num)

class Graph:
    def __init__(self):
        self.nodes = OrderedDict()
    
    def add_node(self,num):
        node = Node(num)
        self.nodes[num] = node
        return node
    
    def add_edge(self,source, destination, weight=0):
        if source or destination not in self.nodes:
            print('Nodes not in Graph')
            return
        else:
            self.nodes[source].adjacent[destination] = weight

g = Graph()
g.add_node(0)
g.add_node(1)
g.add_node(2)

g.add_edge(0,1,3)
g.add_edge(0,2,5)
for i in g.nodes:
    print(f"{i} has connections: {g.nodes[i].adjacent}")
