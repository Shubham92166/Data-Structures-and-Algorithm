'''
Approach:
In a BST, a node at which the both the nodes belong to two differen subtree is the LCA. So, we keep traversin the tree until both the 
given nodes belong to either left subtree or right subtree. When we find that one given node belongs to left subtree and another one in
the right subtree that means the current root node is the LCA so we store it in a variable and return it.
'''

import sys
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")

from createBinaryTree import *

tree = BinaryTee()

class Solution:
    def __init__(self):
        self.lca = None

    def lowestCommonAncestor(self, root, p, q):
        self.helper(root, p, q)
        return self.lca.val
    
    def helper(self, root, p, q):
        if not root:
            return 
        
        elif p < root.val and q < root.val:
            self.helper(root.left, p, q)
        
        elif p > root.val and q > root.val:
            self.helper(root.right, p, q)
            
        else:
            self.lca = root
            return self.lca

#Complexity:
#Time: O(n)
#Space: O(h)
#Where n is the no. of nodes and h is the height of the BST. O(h) can be O(n) in worst case

#Test Cases:
#[6,2,8,0,4,7,9,-1,-1,3,5,-1,-1,-1,-1,-1,-1,-1,-1], 2, 8
#[2,1,-1,-1,-1], 2, 1

root = tree.createBinaryTree([6,2,8,0,4,7,9,-1,-1,3,5,-1,-1,-1,-1,-1,-1,-1,-1])
sol1 = Solution()
print(sol1.lowestCommonAncestor(root, 2, 8))

root = tree.createBinaryTree([2,1,-1,-1,-1])
sol2 = Solution()
print(sol2.lowestCommonAncestor(root, 2, 1))

#Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/