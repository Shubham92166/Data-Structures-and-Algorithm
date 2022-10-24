import sys
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")

from createBinaryTree import *

tree = BinaryTee()

class Solution:
    def __init__(self):
        self.inorder = []
        
    def findTarget(self, root, k):
        self.helper(root)
        
        i, j = 0, len(self.inorder)-1
        
        while i < j:
            if self.inorder[i] == None:
                i += 1

            if self.inorder[j] == None:
                j -= 1

            sum = self.inorder[i] + self.inorder[j]
            if sum > k:
                j -= 1
            elif sum < k:
                i += 1
            else:
                return True
        return False
    
    def helper(self, root):
        if not root:
            return 
        
        self.helper(root.left)
        self.inorder.append(root.val)
        self.helper(root.right)

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[5,3,6,2,4,None,7], 9
#[5,3,6,2,4,None,7], 28

sol = Solution()

root = tree.createBinaryTree([5,3,6,2,4,None,7])
print(sol.findTarget(root, 9))

root = tree.createBinaryTree([5,3,6,2,4,None,7])
print(sol.findTarget(root, 28))

#Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/