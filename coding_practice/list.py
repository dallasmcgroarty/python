class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List(Node):
    def __init__(self):
        self.head = None
        self.length = 0
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

L = List()

a = Node(1)
b = Node(2)
L.head = a
a.next = b
b.next = Node(3)

L.printList()