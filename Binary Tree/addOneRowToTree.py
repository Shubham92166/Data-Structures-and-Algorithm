'''
Approach:
We traverse the whole tree and while traversing we maintain the variable level which indicates the current level at which we are. If 
current level == depth-1 then we add a node on cuurent root's left subtree and right subtree but by attaching new nodes to current root
left and right and then we attach the root's original root's left subtree and right subtree to newly added node. There is a special case,
since the root of the tree is at depth 1. This means that if we try to add a node at depth-1 then there is no such node. So, in this 
case, we make the newly created node as the new root node of the tree and we add original tree as the left subtree of new root. 
'''

from createBinaryTree import *

tree = BinaryTee()

def addOneRow(root, val, depth):
    if not root:
        return None
    level = 1

    if depth == 1:
        leftSubTree = root
        root = TreeNode(val)
        root.left = leftSubTree
        return root

    addRow(root, level, val, depth)
    return root

def addRow(root, level, val, depth):
    if not root:
        return None

    if level == depth-1:
        leftSubTree = root.left
        root.left = TreeNode(val)
        root.left.left = leftSubTree

        rightSubTree = root.right
        root.right = TreeNode(val)
        root.right.right = rightSubTree
        
    addRow(root.left, level + 1, val, depth)
    addRow(root.right, level + 1, val, depth)

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) in worst case can be O(n). h is the height and n is the no. of nodes

#Test Cases:
#[4,2,6,3,1,5, -1, -1, -1, -1, -1, -1, -1], 1, 2
#[4,2,-1,3,1,-1,-1,-1,-1], 1, 3

root = tree.createBinaryTree([4,2,6,3,1,5, -1, -1, -1, -1, -1, -1, -1])
root = addOneRow(root, 1, 2)
print(tree.printTree(root))

root = tree.createBinaryTree([4,2,-1,3,1,-1,-1,-1,-1])
root = addOneRow(root, 1, 3) 
print(tree.printTree(root))  
        
#Link: https://leetcode.com/problems/add-one-row-to-tree/