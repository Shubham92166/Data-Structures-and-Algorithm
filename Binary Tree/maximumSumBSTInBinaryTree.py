import math
class Solution:
    def maxSumBST(self, root):
        self.ans = 0
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root:
            return True, -math.inf, math.inf, 0
        
        lflag, lmax, lmin, ltotal = self.helper(root.left)
        rflag, rmax, rmin, rtotal = self.helper(root.right)
        
        if lflag and rflag and lmax < root.val < rmin:
            total = ltotal + rtotal + root.val
            self.ans = max(self.ans, total)
            return True, max(rmax, root.val), min(lmin, root.val), total
       
        return False, math.inf, -math.inf, 0

#Complexity:
#Time: O(n)
#Space: O(h)
#where in worst case O(h) can be O(n). h is the height and n is the no of nodes

#Test Cases:
#[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6], [4,3,null,1,2], [-4,-2,-5]

#Link: https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

