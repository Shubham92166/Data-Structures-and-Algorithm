'''
Approach: 
We check if the roots value is equal to the sum of it's left child's value and right child's value.
'''

from logging import root
from createBinaryTree import *

tree = BinaryTee()

def checkTree(root):
    if root.val == root.left.val + root.right.val:
        return True
    else:
        return False

#Complexity:
#Time: O(1)
#Space: O(1)

#Test Cases:
#[10,4,6,-1,-1,-1,-1], [5,3,1,-1,-1,-1,-1]

root = tree.createBinaryTree([10,4,6,-1,-1,-1,-1])
print(checkTree(root))

root = tree.createBinaryTree([5,3,1,-1,-1,-1,-1])
print(checkTree(root))

#Link: https://leetcode.com/problems/root-equals-sum-of-children/