# Node and List implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List(Node):
    def __init__(self):
        self.head = None
        self.length = 0
    
    def add_back(self, value):
        if not self.head:
            if isinstance(value, Node):
                self.head = value
            else:
                self.head = Node(value)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            if isinstance(value, Node):
                temp.next = value
            else:
                temp.next = Node(value)
        self.length += 1
    
    def add_front(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
        self.length +=1 

    def __len__(self):
        return self.length
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value, end=' ')
            temp = temp.next

    def cycle_check_print(self):
        seen = set()
        temp = self.head
        while temp:
            if temp in seen:
                print('cycle detected, exiting loop')
                return True
            seen.add(temp)
            print(temp.value, end=' ')
            temp = temp.next
        return False

l = List()
loop = Node(2)
l.add_back(1)
l.add_back(3)
l.add_back(loop)
l.add_back(5)
l.add_front(6)
l.add_front(8)
l.add_back(loop)
#l.print_list()
print()
print(len(l))
l.cycle_check_print()
print()

# Node and Tree implementation 
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.count = 1
        self.leftChild = None
        self.rightChild = None
    
class Tree(TreeNode):
    def __init__(self):
        self.root = None
        self.size = 0
    
    def add_node(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            temp = self.root
            while temp:
                if value < temp.value:
                    if temp.leftChild == None:
                        temp.leftChild = TreeNode(value)
                        self.size += 1
                        return
                    temp = temp.leftChild
                elif value > temp.value:
                    if temp.rightChild == None:
                        temp.rightChild = TreeNode(value)
                        self.size += 1
                        return
                    temp = temp.rightChild
                else:
                    # found duplicate, increment count
                    temp.count += 1
    
    def find(self, value):
        temp = self.root
        while temp:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.leftChild
            else:
                temp = temp.rightChild
        return False
    
    def inorder(self, t):
        if t.leftChild:
            self.inorder(t.leftChild)
        print(t.value)
        if t.rightChild:
            self.inorder(t.rightChild)

    def height(self, t):
        if t is None:
            return 0
        else:
            return 1 + max(self.height(t.leftChild), self.height(t.rightChild))

t = Tree()
t.add_node(8)
t.add_node(5)
t.add_node(10)
t.add_node(7)
t.inorder(t.root)
print(t.height(t.root))
print()

# graph node and graph implementation

class Vertex:
    def __init__(self, key):
        self.key = key
        self.connectedTo = {}

class Graph(Vertex):
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vertList[key] = new_vertex
        self.numVertices += 1
    
    def add_edge(self, v1, v2, cost=0):
        if v1 and v2 not in self.vertList:
            print('Vertices not in Vertex List')
            return
        self.vertList[v1].connectedTo[v2] = cost
    
    def getVertices(self):
        return self.vertList.keys()

    def print_graph(self):
        for v in self.vertList:
            print(f"{v} has connections {self.vertList[v].connectedTo}")

g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_edge(1,2,4)
print(g.getVertices())
g.print_graph()
