# depth first search:
# algorithm to traverse a graph by going down each branch and visiting all children
# before backtracking
# method:
# 1. make the current vertex as visited
# 2. explore each adjacent vertex that is not included in the visited set

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

def dfs(start, target):
    visitedNodes = set()
    stack = [start]

    while len(stack) > 0:
        node = stack.pop()
        if node in visitedNodes:
            continue
        visitedNodes.add(node)
        if node.value == target:
            return True
        
        for n in node.adjacentNodes:
            if n not in visitedNodes:
                stack.append(n)
    return False

print(dfs(a,5))