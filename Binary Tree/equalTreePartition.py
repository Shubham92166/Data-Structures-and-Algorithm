import sys
sys.setrecursionlimit(10**6)

class Solution:
   
    def solve(self, A):
        sums = set()
        total = self.helper(A, sums)
        if total % 2 != 0:
            return 0
        else:
            if total//2 in sums:
                return 1
            return 0
    
    def helper(self, root, sums):
        if not root:
            return 0
        
        leftSum = self.helper(root.left, sums)
        rightSum = self.helper(root.right, sums)
        sums.add(leftSum)
        sums.add(rightSum)
        return leftSum + rightSum + root.val

#Complexity:
#Time: O(n)
#Space: O(n)

#Link: https://www.geeksforgeeks.org/check-if-removing-an-edge-can-divide-a-binary-tree-in-two-halves/