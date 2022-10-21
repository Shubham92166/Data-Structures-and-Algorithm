#Approach:
#We do DFS traversal on the given tree. If the current node is the leaf node and it's value is 0 then we return True. If it is the leaf
#node but it's value is non zero then we return False. +
#If the current node is a non leaf node and node's value is 2 then we take OR of left subtree and right subtree. Else we take the AND of
#left subtree and right subtree.

from createBinaryTree import *

tree = BinaryTee()

def evaluateTree(root):
    return helper(root)

def helper(root):
    if not root.left and not root.right:
        if root.val == 0:
            return False
        else:
            return True
    
    if root.val == 2:
        return helper(root.left) or helper(root.right)
    else:
        return helper(root.left) and helper(root.right)

#Complexity:
#Time: O(n)
#Space: O(h) or O(log n)
#where h is height of binary tree. Since the given tree is full binary tree so h is log n.

#Test Cases:
#[2,1,3,-1,-1,0,1,-1,-1,-1,-1], [0,-1,-1]

root = tree.createBinaryTree([2,1,3,-1,-1,0,1,-1,-1,-1,-1])
print(evaluateTree(root))

root = tree.createBinaryTree([0,-1,-1])
print(evaluateTree(root))

#Link: https://leetcode.com/problems/evaluate-boolean-binary-tree/