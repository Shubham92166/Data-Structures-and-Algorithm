import sys
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")

from createBinaryTree import *

tree = BinaryTee()

def bstFromPreorder(preorder):    
    root = TreeNode(preorder[0])
    stack = [root]
    
    for i in range(1, len(preorder)):
        newNode = TreeNode(preorder[i])
        
        if preorder[i] < stack[-1].val:
            stack[-1].left = newNode
            stack.append(newNode)
            
        else:

            while stack and stack[-1].val < preorder[i]:
                prev = stack.pop()

            prev.right = newNode
            stack.append(newNode)
            
    return root

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[8,5,1,7,10,12], [1,3]

#Link: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/