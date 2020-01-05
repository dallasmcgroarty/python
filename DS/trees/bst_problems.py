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
