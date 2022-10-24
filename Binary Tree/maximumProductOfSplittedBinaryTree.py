class Solution:
    def maxProduct(self, root): 
        totalSum = 0
        self.maxProd = 0
        totalSum = self.sumOfAllNodes(root)
        self.Product(root, totalSum)
        return self.maxProd % ((10**9) + 7)
    
    def sumOfAllNodes(self, root):
        if not root:
            return 0
        
        return self.sumOfAllNodes(root.left) + self.sumOfAllNodes(root.right) + root.val
    
    def Product(self, root, total):
        if not root:
            return 0
        leftSum = self.Product(root.left, total)
        rightSum = self.Product(root.right, total)
        
        subTreeSum = leftSum + rightSum + root.val
        self.maxProd = max(self.maxProd, (total-subTreeSum)*subTreeSum)
        return subTreeSum
    
#Complexity:
#Time: O(n)
#Space: O(h)
#Where O(h) in worst case can be O(n). n is the no. of nodes and h is the height of tree

#Link: https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/