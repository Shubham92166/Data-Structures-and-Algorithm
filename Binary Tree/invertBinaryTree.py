'''
Approach: 
We traverse the whole tree and swap the left subtree and right subtree and return the root node
'''

from createBinaryTree import *

tree = BinaryTee()

def invertTree(root):
    if not root:
        return None
    leftTree = root.left
    root.left = root.right
    root.right = leftTree

    invertTree(root.left)
    invertTree(root.right)

    return root

#Complexity:
#Time: O(n)
#Space: O(h)
#Where n is the no. of nodes and h is the height. O(h) in worst case can be O(n). 

#Test Cases
#[4,2,7,1,3,6,9,-1,-1,-1,-1,-1,-1,-1,-1], [2,1,3,-1,-1,-1,-1], [-1]

root = tree.createBinaryTree([4,2,7,1,3,6,9,-1,-1,-1,-1,-1,-1,-1,-1])
root = invertTree(root)
print(tree.printTree(root))

root = tree.createBinaryTree([2,1,3,-1,-1,-1,-1])
root = invertTree(root)
print(tree.printTree(root))

root = tree.createBinaryTree([-1])
root = invertTree(root)
print(tree.printTree(root))

#Link: https://leetcode.com/problems/invert-binary-tree/
