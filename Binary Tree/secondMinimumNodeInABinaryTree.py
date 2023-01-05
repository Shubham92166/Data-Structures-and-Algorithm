from createBinaryTree import *

tree = BinaryTee()

class Solution:
    def findSecondMinimumValue(self, root):
        self.firstMinimum, self.secondMinimum = 999999999999, 999999999999
        
        self.getSecondMinimum(root)
        
        return self.secondMinimum if self.secondMinimum != 999999999999 else -1

    def getSecondMinimum(self, root):
        if not root:
            return 

        if root.val < self.firstMinimum:
            self.secondMinimum = self.firstMinimum 
            self.firstMinimum = root.val

        if root.val < self.secondMinimum and root.val != self.firstMinimum:
            self.secondMinimum = root.val
        
        self.getSecondMinimum(root.left)
        self.getSecondMinimum(root.right)

#Complexity:
#Time: O(n)
#Space: O(h)
#Where n is the no. of nodes and h is the height of the binary tree. In worst case, h can be n

#Test Cases:
#[2,2,5,-1,-1,5,7,-1,-1,-1,-1], [2,2,2,-1,-1,-1,-1]

root = tree.createBinaryTree([2,2,5,-1,-1,5,7,-1,-1,-1,-1])
sol = Solution()
print(sol.findSecondMinimumValue(root))

root = tree.createBinaryTree([2,2,2,-1,-1,-1,-1])
sol = Solution()
print(sol.findSecondMinimumValue(root))

#Link: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/