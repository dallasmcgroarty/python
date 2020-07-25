# breadth first search:
# algorithm for traversing a graph, visit all nodes on the same level before going
# deeper in the graph
from collections import deque
class Node:
    def __init__(self,value):
        self.value = value
        self.adjacentNodes = []

a = Node(1)
b = Node(3)
c = Node(5)
d = Node(6)
a.adjacentNodes.append(b)
a.adjacentNodes.append(d)
b.adjacentNodes.append(c)
c.adjacentNodes.append(d)

def bfs(start, target):
    visitedNodes = set()
    queue = deque([start])

    while len(queue)  > 0:
        node = queue.pop()
        if node in visitedNodes:
            continue

        visitedNodes.add(node)
        if node.value == target:
            return True
        
        for n in node.adjacentNodes:
            if n not in visitedNodes:
                queue.appendleft(n)
    return False

print(bfs(a,3))