# cvent interview practice

def reverse_str(s):
    return s[::-1]

def reverse_str1(s):
    ret_str = ''
    index = len(s)-1
    while index >= 0:
        ret_str += s[index]
        index -= 1
    return ret_str

print(reverse_str1('hello'))

def balance(s):
    if len(s) % 2 != 0:
        return False
    
    stack = []
    opening = set('({[')
    matches = set([('(',')'), ('{','}'), ('[',']')])

    for x in s:
        if x in opening:
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            
            last = stack.pop()

            if (last,x) not in matches:
                return False
    return len(stack) == 0

print(balance('({[]})'))

def coinChange(target, coins):
    min_coins = target
    if target in coins:
        return 1
    else:
        for i in [c for c in coins if c < target]:
            num_coins = 1 + coinChange(target-i, coins)

            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins

print(coinChange(25,[1,2,3,4,5]))

def palindrome(s):
    # rev_str = s[::-1]
    rev_str = ''
    index = len(s)-1
    while index >= 0:
        rev_str += s[index]
        index -= 1

    if s == rev_str:
        return True
    else:    
        return False

print(palindrome('abcba'))

def permute(s):
    out = []

    if len(s) == 1:
        out = [s]
    else:
        for i, letter in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                out += [letter+perm]
    return out

print(permute('abc'))

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class List(Node):
    def __init__(self):
        self.head = None
        self.length = 0
    
    def addBack(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(value)
        self.length += 1
    
    def addFront(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = self.head
            self.head = Node(value)
            self.head.next = temp
        self.length += 1
    
    def __len__(self):
        return self.length

    def printList(self):
        temp = self.head
        while temp:
            print(temp.value,end=' ')
            temp = temp.next
        print()

L = List()
L.addBack(3)
L.addBack(4)
L.addFront(2)
L.printList()
print(len(L))

