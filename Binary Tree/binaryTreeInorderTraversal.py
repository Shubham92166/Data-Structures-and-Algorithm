"""
Approach:

Inorder traversal of binary tree is Left-Root-Right. We have a answer array to store all the nodes. We first call on the left subtree 
then store the root node's val in answer array and then call recursively on the right subtree. At the end, we will have all the nodes 
in our answer array as the inorder order traversal of the binary tree.
"""

from createBinaryTree import *

tree = BinaryTee()

def inorderTraversal(root):
    ans = []
    inorder(root, ans)
    return ans 

def inorder(root, ans):
    if not root:
        return None
        
    inorder(root.left, ans)
    ans.append(root.val)
    inorder(root.right, ans)

#Complexity:
#Time: O(n)
#Space: O(h)
#where in worst case O(h) can be O(n). h is the height and n is the number of nodes

#Test Cases:
#[1,-1,2,3,-1,-1,-1], [], [1, -1, -1]

root = tree.createBinaryTree([1,-1,2,3,-1,-1,-1])
print(inorderTraversal(root))

root = tree.createBinaryTree([])
print(inorderTraversal(root))

root = tree.createBinaryTree([1, -1, -1])
print(inorderTraversal(root))

#Link: https://leetcode.com/problems/binary-tree-inorder-traversal/