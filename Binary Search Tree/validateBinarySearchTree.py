'''
Approach:
As per the question, left child is less than the root node and right child is greater than the root node. So, we take two values as l 
and r and initially they are -infinity and +inifinity. We traverse the whole tree in the top-down fashion and check whether the left child has a value less than
the root node and right child has a value greater than the root node. If this condition is True then we call of it's left subtree and 
right subtree else we return False. 
While calling for left child, the r (maximum value) should be less than the root node but l (minimum value) can be anything. Similarly,
for right subtree, the l (minimum value) should be greater than root node's value and r (maximum value) can be anything.
'''

import sys
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")

from createBinaryTree import *

tree = BinaryTee()

import math
def isValidBST(root):
        return helper(root, -math.inf, math.inf)
        
def helper(root, l, r):
    if not root:
        return True
    if root.val >= l and root.val <= r:
        left = helper(root.left, l, root.val-1) 
        right = helper(root.right, root.val+1, r)
        return left and right
    else:
        return False
    
#Complexity:
#Time: O(n) 
#Space: O(h)
#Where n is the no. of nodes and h is the height of the BST. O(h) in worst case could be O(n)

#Test Cases:
#[2,1,3,-1,-1,-1,-1], [5,1,4,-1,-1,3,6,-1,-1,-1,-1]

root = tree.createBinaryTree([2,1,3,-1,-1,-1,-1])
print(isValidBST(root))

root = tree.createBinaryTree([5,1,4,-1,-1,3,6,-1,-1,-1,-1])
print(isValidBST(root))

#Link: https://leetcode.com/problems/validate-binary-search-tree/