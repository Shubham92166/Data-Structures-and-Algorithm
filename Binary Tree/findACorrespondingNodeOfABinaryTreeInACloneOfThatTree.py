class Solution:
    def getTargetCopy(self, original, cloned, target):
        self.ans = -1
        self.helper(cloned, target, self.ans)
        return (self.ans)
    
    def helper(self, root, target, ans):
        if not root:
            return  
       
        if root.val == target.val:
            self.ans = root
            return 
        
        self.helper(root.left, target, ans) 
        self.helper(root.right, target, ans)

#Complexity:
#Time: O(n)
#Space: O(h)
#Where O(h) in worst case can be O(n). n is the no. of nodes and h is the height of the tree

#Test Cases:
#[7,4,3,null,null,6,19], 3
#[7], 7
#[8,null,6,null,5,null,4,null,3,null,2,null,1], 4

#Link: https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
