# function to check for a cycle in a linked list
# the node class defined below:
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def cycle_check(node):
    temp = node
    while(temp):
        if temp.next == node:
            return True
        else:
            temp = temp.next
    return False

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = a # cycle created for testing

print('cycle in linked list => ', cycle_check(a))

def print_list(head):
    temp = head
    while(temp):
        print(temp.value, end=' ')
        temp = temp.next
    print()
a2 = Node(1)
b2 = Node(2)
c2 = Node(3)
d2 = Node(4)
e2 = Node(5)

a2.next = b2
b2.next = c2
c2.next = d2
d2.next = e2

# reverse a linked list
def reverse_list(head):
    current = head
    prev = None
    next = None

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

reverse_list(a2)
print(d2.next.value)
print(c2.next.value)
print(b2.next.value)

reverse_list(e2)
# print the length of the linked list/number of nodes in the list
def list_size(head):
    temp = head
    count = 0
    while(temp):
        count += 1
        temp = temp.next
    return count

print('size of list => ', list_size(a2))

# function thate takes a head node and an integer n and returns the
# nth to last node in the linked list
def nth_last_node(n, head):
    temp = head
    count = 0
    while(temp):
        count += 1
        temp = temp.next
    if n > count:
        raise LookupError('Error: n greater than length of list')
    target = count - n
    nth = head
    while(nth and target > 0):
        nth = nth.next
        target -= 1
    return nth

print_list(a2)
nth_node = nth_last_node(3, a2)
print(nth_node.value)