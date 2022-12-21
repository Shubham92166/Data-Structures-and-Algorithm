'''
Approach: 
We create an empty array/list to store the nodes. We call recursive function, we append the current node's value and then call 
recursively for left subtree and right subtree. At the end, we return the array/list. 
'''

from createBinaryTree import *

tree = BinaryTee()

def preorderTraversal(root):
        ans = []
        preOrder(root, ans)
        return ans

def preOrder(root, ans):
    if not root:
        return []

    ans.append(root.val)
    
    preOrder(root.left, ans)
    preOrder(root.right, ans)

#Complexity:
#Time: O(n)
#Space: O(h)
#where n is the no. of nodes and h is the height of the tree. In worst case, h will be n.

#Test Cases:
#[1,-1,2,3,-1,-1,-1], [], [1]

root = tree.createBinaryTree([1,-1,2,3,-1,-1,-1])
print(preorderTraversal(root))

root = tree.createBinaryTree([-1])
print(preorderTraversal(root))

root = tree.createBinaryTree([1,-1,-1])
print(preorderTraversal(root))

#Link: https://leetcode.com/problems/binary-tree-preorder-traversal/