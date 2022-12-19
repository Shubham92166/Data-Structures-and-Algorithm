'''
Approach: In the BST, we tree to search the node which is to be inserted. When we reach the leaf node and we couldnt find the given node
then we simply return the new node with the given value. It then gets attached to its correct position.
'''

import sys
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")

from createBinaryTree import *

tree = BinaryTee()

def insertIntoBST(root, val):
    if not root:
        node = TreeNode(val)
        return node
    if root.val > val:
        root.left = insertIntoBST(root.left, val)
        return root
    if root.val <= val:
        root.right = insertIntoBST(root.right, val)
        return root

#Complexity:
#Time: O(h)
#Space: O(h)
#where h is the height of the tree. In worst case O(h) can be O(n) and n is the no. of nodes

#Test Cases:
#[4,2,7,1,3,-1,-1,-1,-1,-1,-1], 5
#[40,20,60,10,30,50,70,-1,-1,-1,-1,-1,-1,-1,-1], 25
#[4,2,7,1,3,-1,-1,-1,-1,-1,-1], 5

root = tree.createBinaryTree([4,2,7,1,3,-1,-1,-1,-1,-1,-1])
newRoot = insertIntoBST(root, 5)
print(tree.printTree(newRoot))

root = tree.createBinaryTree([40,20,60,10,30,50,70,-1,-1,-1,-1,-1,-1,-1,-1])
newRoot = insertIntoBST(root, 25)
print(tree.printTree(newRoot))

root = tree.createBinaryTree([4,2,7,1,3,-1,-1,-1,-1,-1,-1])
newRoot = insertIntoBST(root, 5)
print(tree.printTree(newRoot))

#Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/

        