class Solution:
    def __init__(self):
        self.sum = 0
    def rangeSumBST(self, root, low, high):
        if not root:
            return 
        if low <= root.val <= high:
            self.sum += root.val
        
        self.rangeSumBST(root.left, low, high)
        self.rangeSumBST(root.right, low, high)
        return self.sum
    
#Complexity:
#Time: O(n)
#Space: O(H)
#where H can be O(n) is worst case and n is the no. of nodes

#Test Cases:
#[10,5,15,3,7,null,18], 7, 15
#[10,5,15,3,7,13,18,1,null,6], 6, 10

#Link: https://leetcode.com/problems/range-sum-of-bst/