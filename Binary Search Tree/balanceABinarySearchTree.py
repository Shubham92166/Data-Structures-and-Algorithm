class Solution:
    def balanceBST(self, root):
        inorder = []
        self.findInorder(root, inorder)
        return self.constructTree(inorder)
        
    def findInorder(self, root, inorder):
        if not root:
            return
        
        self.findInorder(root.left, inorder)
        inorder.append(root.val)
        self.findInorder(root.right, inorder)
    
    def constructTree(self, nums):
        if not nums:
            return 
        
        midIndex = len(nums)//2
        root = TreeNode(nums[midIndex])
        root.left = self.constructTree(nums[:midIndex])
        root.right = self.constructTree(nums[midIndex+1:])
        return root

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1,null,2,null,3,null,4,null,null], [2,1,3]

#Link: https://leetcode.com/problems/balance-a-binary-search-tree/
        