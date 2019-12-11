class Deque(object):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop(0)

    def addBack(self, item):
        self.items.append(item)

    def removeBack(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

d = Deque()

d.addFront('hello')
d.addBack('world')

print(d.size())

print(d.removeFront() + ' ' + d.removeBack())

print(d.isEmpty())