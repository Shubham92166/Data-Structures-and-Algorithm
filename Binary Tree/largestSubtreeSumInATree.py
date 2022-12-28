from createBinaryTree import *

tree = BinaryTee()

class Solution:
    def __init__(self):
        self.maxSum = -999999
    
    def findLargestSubtreeSum(self, root):
        if not root:
            return 0
        
        self.find(root)
        return self.maxSum
    
    def find(self, root):
        if not root:
            return 0
        
        sumOfAll = self.find(root.left) + self.find(root.right) + root.val
        
        self.maxSum = max(self.maxSum, sumOfAll)
        
        return sumOfAll

#Complexity:
#Time: O(n)
#Space: O(h)
#Where n is the no. of nodes and h is the height of the tree. In worst case, h can be equal to n

#Test Cases:
#[1,2,3,4,5,6,7,-1,-1,-1,-1,-1,-1,-1,-1], [1,-2,3,4,5,-6,2,-1,-1,-1,-1,-1,-1,-1,-1]

root = tree.createBinaryTree([1,2,3,4,5,6,7,-1,-1,-1,-1,-1,-1,-1,-1])
sol = Solution()
print(sol.findLargestSubtreeSum(root))

root = tree.createBinaryTree([1,-2,3,4,5,-6,2,-1,-1,-1,-1,-1,-1,-1,-1])
sol = Solution()
print(sol.findLargestSubtreeSum(root))

#Link: https://practice.geeksforgeeks.org/problems/largest-subtree-sum-in-a-tree/1

