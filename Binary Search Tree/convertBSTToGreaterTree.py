import sys
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")

from createBinaryTree import *

tree = BinaryTee()

class Solution:
    def convertBST(self, root):
        self.sum = 0
        self.helper(root)
        return root
    
    def helper(self, root):
        if not root:
            return 
        self.helper(root.right)
        
        temp = root.val
        root.val += self.sum 
        self.sum += temp
        
        self.helper(root.left)
        

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) in worst can be O(n)

#Test Cases:
#[4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
#[0,None,1]

#Link: https://leetcode.com/problems/convert-bst-to-greater-tree/
