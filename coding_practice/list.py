class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List(Node):
    def __init__(self):
        self.head = None
        self.length = 0
    
    def addBack(self, value):
        if self.length == 0:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)
        self.length += 1
    
    def addFront(self,value):
        if self.length == 0:
            self.head = Node(value)
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp

    def __len__(self):
        return self.length

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def __repr__(self):
        return f"List of {len(self)} nodes"

    def cycle_check(self):
        seen = set()
        temp = self.head
        while temp:
            if temp in seen:
                return True
            seen.add(temp)
            temp = temp.next
        return False

L = List()

L.addBack(3)
L.addBack(2)
L.addBack(5)
L.addBack(6)
L.addFront(1)
L.addFront(0)
# a = Node(1)
# b = Node(2)
# L.head = a
# a.next = b
# b.next = Node(3)
print('length of list: ',len(L))

L.printList()

print(L)