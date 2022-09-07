import sys
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")

from createBinaryTree import *

tree = BinaryTee()

class Solution:
    def __init__(self):
        self.k = 0
        self.ans = -1
        
    def kthSmallest(self, root, k):
        self.k = k
        self.helper(root)
        return self.ans
    
    def helper(self, root):
        if not root:
            return 
        
        self.helper(root.left)
        
        self.k -= 1
        
        if self.k == 0:
            self.ans = root.val
            return
        
        self.helper(root.right)

#Complexity:
#Time: O(h)
#Space: O(h)
#Where O(h) can be O(n) in worst case

#Test Cases:
#[3,1,4,None,2], 1
#[5,3,6,2,4,None,None,1], 3

sol = Solution()

root = tree.createBinaryTree([3,1,4,None,2])
print(sol.kthSmallest(root, 1))

root = tree.createBinaryTree([5,3,6,2,4,None,None,1])
print(sol.kthSmallest(root, 3))

#Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/


