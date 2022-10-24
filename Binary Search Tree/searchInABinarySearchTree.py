#Approach:
#Since the given tree is a BST. Then we make the use of BST property that all the elements on the left subtree of the root will be less
#than or equal to the root and all the elements on the right subtree will be greater than the root. This will help us to reduce the 
#search space

import sys

sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")

from createBinaryTree import *

tree = BinaryTee()

def searchBST(root, val):
    if not root:
        return root
    if root.val == val:
        return root.val
    elif root.val > val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)

#Complexity:
#Time: O(h)
#Space: O(h)

#Test Cases:
#[4,2,7,1,3,-1,-1,-1,-1,-1,-1], 2
#[4,2,7,1,3], 5

root = tree.createBinaryTree([4,2,7,1,3,-1,-1,-1,-1,-1,-1])
print(searchBST(root, 2))

root = tree.createBinaryTree([4,2,7,1,3,-1,-1,-1,-1,-1,-1])
print(searchBST(root, 5))

#Link: https://leetcode.com/problems/search-in-a-binary-search-tree/