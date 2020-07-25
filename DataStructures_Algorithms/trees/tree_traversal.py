# traversing a tree
# 3 patternes used
# preorder, inorder, postorder
# traversals better used as external from the tree class


# preorder - root node first, then recursive preorder on left,
# then recursive preorder on right

# inorder - recursive inorder on left, visit root, then recursive inorder on right

# postorder - recursive postorder on left, then right, then visit root

from nodes_tree import *

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

print()
preorder(t)
print()
postorder(t)