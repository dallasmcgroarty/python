class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None


class BST:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def length(self):
        return self.size
    
    def addNode(self, value):
        if self.root == None:
            self.root = Node(value)
            self.size += 1
        else:
            temp = self.root
            while temp:
                if value < temp.value:
                    if temp.leftChild == None:
                        temp.leftChild = Node(value)
                        self.size += 1
                        return
                    temp = temp.leftChild
                elif value > temp.value:
                    if temp.rightChild == None:
                        temp.rightChild = Node(value)
                        self.size += 1
                        return
                    temp = temp.rightChild
        
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
    
    def min(self):
        temp = self.root
        while temp:
            if temp.leftChild == None:
                return temp.value
            else:
                temp = temp.leftChild
    
    def max(self):
        temp = self.root
        while temp:
            if temp.rightChild == None:
                return temp.value
            else:
                temp = temp.rightChild
    
    def height(self, t):
        if t is None:
            return 0
        else:
            return 1 + max(self.height(t.leftChild), self.height(t.rightChild))
        
    def inorder(self,t):
        if t.leftChild:
            self.inorder(t.leftChild)
        print(t.value)
        if t.rightChild:
            self.inorder(t.rightChild)
   

t = BST()
t.addNode(5)
t.addNode(6)
t.addNode(4)
t.addNode(7)
t.addNode(3)
t.addNode(2)
t.inorder(t.root)
print(t.find(1))
print('min value in tree -> ', t.min())
print('max value in tree -> ', t.max())
print('size of tree is -> ', len(t))
print('height of tree -> ', t.height(t.root))