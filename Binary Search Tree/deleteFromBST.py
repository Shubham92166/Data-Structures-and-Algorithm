'''
Approach:
We first find the node which needs to be deleted. Since, it is a BST so we don't need to traverse the whole tree instead at each level
we just need to traverse only one subtree depending upon the BST property. After finding the node there are three conditions:
Let's say the node to be deleted it called as target node
1. Target node is a leaf node- in this case, we simply return Null or None (in python)
2. Target node has anyone child i.e., either left or right child- in this case, whichever child is present we simply return that
3. Target node has both children- in this case, we take the smallest node from the right subtree of the target node and replaces the 
value of the target node to smallest node and then we delete the smallest node from the right subtree.
'''
import sys
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")

from createBinaryTree import *

tree = BinaryTee()

def deleteNode(root, key):
    if not root:
        return None

    if root.val > key:
        newLeft = deleteNode(root.left, key)
        root.left = newLeft
        return root

    if root.val < key:
        newRight = deleteNode(root.right, key)
        root.right = newRight
        return root

    if not root.left and not root.right:
        return None

    if not root.left:
        return root.right

    if not root.right:
        return root.left

    minNode = MinNode(root.right)
    root.val = minNode

    root.right = deleteNode(root.right, minNode)
    return root
    
def MinNode(root):
    if not root:
        return 10000

    if not root.left:
        return root.val

    return MinNode(root.left)

#Complexity:
#Time: O(h)
#Space: O(h)
#Where h is the height of the tree. In worst case, h can be n where n is the no. of nodes

#Test Cases:
#[5,3,6,2,4,-1,7,-1,-1,-1,-1,-1,-1], 3
#[5,3,6,2,4,-1,7,-1,-1,-1,-1,-1,-1], 0
#[], 0

root = tree.createBinaryTree([5,3,6,2,4,-1,7,-1,-1,-1,-1,-1,-1])
newRoot = deleteNode(root, 3)
print(tree.printTree(newRoot))

root = tree.createBinaryTree([5,3,6,2,4,-1,7,-1,-1,-1,-1,-1,-1])
newRoot = deleteNode(root, 0)
print(tree.printTree(newRoot))

root = tree.createBinaryTree([-1])
newRoot = deleteNode(root, 0)
print(tree.printTree(newRoot))

#Link: https://leetcode.com/problems/delete-node-in-a-bst/description/