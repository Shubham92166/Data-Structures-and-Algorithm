'''
Approach:

The concept here is if the sum of all nodes is odd then we can we cannot partition it. If is even then it can be partition. However, a 
subtree should have a half of the total sum. So, For every subtree, we calculate it's sum of nodes value and store it in a hashset. Then
we will check if the total sum is odd or even. If it is odd then we simply return False (0) else we will check if half of total sum 
exists in hashset. If it exists then we return True (1) else we return False (0).
'''

import sys
sys.setrecursionlimit(10**6)

from createBinaryTree import *

tree = BinaryTee()

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
#Space: O(h)
#Where O(h) can be O(n) in worst case. h is the height and n is the no. of nodes

#Test Cases:
#[5,3,7,4,6,5,6,-1,-1,-1,-1,-1,-1,-1,-1], [1,2,10,-1,-1,20,2,-1,-1,-1,-1]

sol = Solution()

root = tree.createBinaryTree([5,3,7,4,6,5,6,-1,-1,-1,-1,-1,-1,-1,-1])
print(sol.solve(root))

root = tree.createBinaryTree([1,2,10,-1,-1,20,2,-1,-1,-1,-1])
print(sol.solve(root))

#Link: https://www.geeksforgeeks.org/check-if-removing-an-edge-can-divide-a-binary-tree-in-two-halves/