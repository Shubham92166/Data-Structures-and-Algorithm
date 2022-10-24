"""
Aprroach: We need to find the count of nodes which are smaller than all the nodes in it's path starting from the root node. So, at each
node, we check if the current node is greater than the greater node or not. If it is greater then we store the current node as the 
greater node and increment the count. We do this process recursively for left subtree and right subtree.
"""

from createBinaryTree import *

tree = BinaryTee()

def goodNodes(root):
        return goodNode(root, root.val)

def goodNode(root, greater_node):
    count = 0
    if not root: return 0
    if root.val >= greater_node:
        greater_node = root.val 
        count += 1
    return count + goodNode(root.left, greater_node) + goodNode(root.right, greater_node)

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) in worst case can be O(n). h is th height and n is the no. of nodes

#Test Cases:
#[3,1,4,3,-1,1,5,-1,-1,-1,-1,-1,-1], [3,3,-1,4,2,-1,-1,-1,-1], [1]

root = tree.createBinaryTree([3,1,4,3,-1,1,5,-1,-1,-1,-1,-1,-1])
print(goodNodes(root))

root = tree.createBinaryTree([3,3,-1,4,2,-1,-1,-1,-1])
print(goodNodes(root))

root = tree.createBinaryTree([1,-1,-1])
print(goodNodes(root))

#Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/