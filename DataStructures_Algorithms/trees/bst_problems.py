# bst problems
from bst import *
# problem 1
# given a binary tree, determine if its a binary search tree or not

def bst_check(tree):
    # binary search tree orders lower to left and greater to right
    # therefore if we do a inorder traversal the values should be sorted
    # if not then we dont have a bst
    values = inorder(tree)

    if sorted(values) == values:
        return True
    else:
        return False

def inorder(tree):
    values = []
    if tree != None:
        inorder(tree.leftChild)
        values.append(tree.value)
        inorder(tree.rightChild)
    return values

# above solution for problem 1 is correct

# problem 2
# given a binary tree of integers, print it in level order
# that is to each level of the tree is on a new line
# ex:        0
#         1    2
#        3 4  5 6
import collections

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

def level_order(tree):
    if not tree:
        return
    
    nodes = collections.deque([tree])

    current_count = 1
    next_count = 0

    while len(nodes) != 0:
        current_node = nodes.popleft()
        current_count -= 1
        
        print (current_node.value, end=' ')

        if current_node.left:
            nodes.append(current_node.left)
            next_count += 1
        if current_node.right:
            nodes.append(current_node.right)
            next_count += 1
        if current_count == 0:
            print ()
            current_count, next_count = next_count, current_count

root = Node(1)
root.left = Node(2)
root.right = Node(3)

level_order(root)

#problem 3 - Trim BST 
# given a tree and a min and max value
# ensure the tree contains values between min and max inclusive

def trim_bst(tree, min_val, max_val):
    if not tree:
        return
    
    # recursive calls to check each branch
    tree.left = trim_bst(tree.left, min_val, max_val)
    tree.right = trim_bst(tree.right, min_val, max_val)

    if min_val <= tree.val <= max_val:
        return tree
    
    # if val is lower than min, return right subtree, because we know
    # everything to the left will be lower, and right is greater
    if tree.val < min_val:
        return tree.right
    
    #if val is greater than max, return left subtree, because we know
    # everythign to the left will be lower, and right is greater
    if tree.val > max_val:
        return tree.left