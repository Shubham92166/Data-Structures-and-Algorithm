from logging import root
from createBinaryTree import *

tree = BinaryTee()

def maxDepth(root):
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

#Complexity:
#Time :O(H)
#Space: O(H)
#where O(H) can be O(n) in worst case and n is the no. of nodes

#Test Cases:
#[3,9,20,null,null,15,7], [1,null,2]

root = tree.createBinaryTree([3,9,20,None,None,15,7])
print(maxDepth(root))

root = tree.createBinaryTree([1,None,2])
print(maxDepth(root))

#Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

    