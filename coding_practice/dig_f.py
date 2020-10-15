# study

# reverse string
def reverse(s):
    ret_str = ''
    i = len(s)-1
    while i >= 0:
        ret_str += s[i]
        i-=1
    return ret_str

print(reverse('hello'))
print()

def find_max(arr):
    current_max = arr[0]
    for num in arr:
        if num > current_max:
            current_max = num
    return current_max

print(find_max([3,5,4,6,9,2]))
print()

def find_min(arr):
    current_min = arr[0]
    for num in arr:
        if num < current_min:
            current_min = num
    return current_min

print(find_min([3,5,4,1,9,2]))
print()

def fizzbuzz(num):
    for i in range(1,num+1):
        if i % 3 == 0 and i % 5 == 0:
            print('Fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

fizzbuzz(15)
print()

def duplicate(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return i
        seen.add(i)
    return -1

print(duplicate([3,4,2,2,1]))
print()

# most frequent item in arr
def frequency(arr):
    freq = {}
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    current_freq = 0
    most_freq = 0
    for x in freq:
        if freq[x] > current_freq:
            current_freq = freq[x]
            most_freq = x
    return most_freq

print(frequency('abccdbbafba')) # = b
print()


# two sum
# given target and arr, find two items that sum to the target
# return first met
def two_sum(arr,target):
    seen = set()
    for num in arr:
        if target - num in seen:
            return [num, target-num]
        seen.add(num)
    return None

print(two_sum([2,3,4,2,5,1],5))
print()

# two sum
# return all matches that sum to target
def two_sum_all(arr,target):
    seen = set()
    matches = []
    for num in arr:
        if target - num in seen:
            matches.append((num,target-num))
        seen.add(num)
    return matches

print(two_sum_all([2,3,4,2,1,5,4,1],3))
print()

#################################
# List data structure
print('---- Python List ----')

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class List(Node):
    def __init__(self):
        self.head = None
        self.length = 0
    
    def addBack(self,val):
        if not self.head:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(val)
        self.length += 1
    
    def addFront(self,val):
        if not self.head:
            self.head = Node(val)
        else:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
        self.length += 1

    def delete(self, val):
        if self.head.val == val:
            self.head = self.head.next
            return
        prev = self.head
        next = self.head.next
        while prev and next:
            if next.val == val:
                prev.next = next.next
                return
            prev = prev.next
            next = next.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next

    def __repr__(self):
        list_str = ''
        temp = self.head
        while temp:
            list_str += str(temp.val) + ' '
            temp = temp.next
        return list_str
    
    def __len__(self):
        return self.length
    
    def cycle_check(self):
        seen = set()
        temp = self.head
        while temp:
            if temp.val in seen:
                return True
            seen.add(temp.val)
            temp = temp.next
        return False

L = List()

L.addBack(2)
L.addBack(3)
L.addFront(1)
L.addBack(2)

L.delete(3)

L.addBack(4)
L.addFront(0)

L.printList()

print(L.cycle_check())
print()
#################################
# BST data structure
print('---- Python BST ----')

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.leftChild = None
        self.rightChild = None

class BST(TreeNode):
    def __init__(self):
        self.root = None
        self.size = 0
    
    def add(self, val):
        if self.root == None:
            self.root = TreeNode(val)
            self.size += 1
        else:
            temp = self.root
            while temp:
                if val < temp.val:
                    if temp.leftChild == None:
                        temp.leftChild = TreeNode(val)
                        self.size += 1
                        return
                    temp = temp.leftChild
                elif val > temp.val:
                    if temp.rightChild == None:
                        temp.rightChild = TreeNode(val)
                        self.size += 1
                        return
                    temp = temp.rightChild
    
    def find(self, val):
        temp = self.root
        while temp:
            if val < temp.val:
                temp = temp.leftChild
            elif val > temp.val:
                temp = temp.rightChild
            else:
                return True
        return False

    def inorder(self,t):
        if t.leftChild:
            self.inorder(t.leftChild)
        print(t.val, end=' ')
        if t.rightChild:
            self.inorder(t.rightChild)

    def min(self):
        temp = self.root
        while temp:
            if temp.leftChild == None:
                return temp.val
            temp = temp.leftChild
        
    def max(self):
        temp = self.root
        while temp:
            if temp.rightChild == None:
                return temp.val
            temp = temp.rightChild

B = BST()
B.add(3)
B.add(4)
B.add(2)
B.add(1)

B.inorder(B.root)

print(B.find(4))

print(B.min())

print()

# user = input('Say something: ')
# print(type(user))