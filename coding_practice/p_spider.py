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
print()
# problem solving

def balance(s):
    if len(s) % 2 != 0:
        return False
    
    stack = []
    opens = set('([{')
    matches = set([('(',')'),('{','}'),('[',']')])

    for x in s:
        if x in opens:
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            
            last = stack.pop()

            if (last, x) not in matches:
                return False
    return len(stack) == 0

print(balance('({[})'))
print()

def rev_str(s):
    ret_str = ''
    index = len(s)-1
    while index >= 0:
        ret_str += s[index]
        index -= 1
    return ret_str

print(rev_str('hello'))
print()

def palindrome(s):
    rev = rev_str(s)
    if rev == s:
        return True
    return False

print(palindrome('tacocat'))
print()

def anagram(s1,s2):
    return sorted(s1) == sorted(s2)

print(anagram('hello','llohe'))
print()

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def gcd(x,y):
    while(y):
        x, y = y, x % y
    return x

def dec_to_bin(n):
    if n > 0:
        dec_to_bin(n//2)
        print(n%2, end='')

dec_to_bin(7)
print()

def two_sum(arr,s):
    seen = set()
    for i in arr:
        diff = s - i
        if diff in seen:
            return [arr.index(diff), arr.index(i)]
        seen.add(i)
    return []

print(two_sum([3,2,1,5,8],7))
print()

def permute(s):
    out = []
    if len(s) == 1:
        out = [s]
    else:
        for i, letter in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [letter+perm]
    return out

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for k in range(0,n-i-1):
            if arr[k] > arr[k+1]:
                arr[k+1],arr[k] = arr[k], arr[k+1]
    return arr

print(bubble_sort([5,3,7,2,8,1]))

# capitalize the first character of each words in a string
def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))

# function accepts a collection, value and start index(optional). return true if 
# the value exists starting the search from the start index, else return false
# if a collection is a dict, look in the values of the dict and ignore start index
def includes(item, val, start=0):
    if type(item) == dict:
        if val in item.values():
            return True
    else:
        for i in range(start,len(item)):
            if item[i] == val:
                return True
    return False

# given a string and number n which represents the characters to truncate
# truncate the string and add '...' to the end if the string if it was truncated
def truncate(string, n):
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    truncate = n-3
    ret_str = ''
    for i in range(0,len(string)):
        if i == truncate:
            ret_str += '...'
            break
        ret_str += string[i]
    return ret_str

# greedy, O(n^2)
def profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = 0

    for price in stock_prices:
        min_price = min(min_price, price)

        compare_profit = price - min_price

        max_profit = max(max_profit, compare_profit)
    return max_profit