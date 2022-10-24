'''
Approach:

For every subtree, we calculate the sum of all the nodes and count of nodes. Then we calculate the average of the subtree. If average of
the subtree is equal to the root's value then we increment our count. At the end, we return the count.
'''

from createBinaryTree import *

tree = BinaryTee()

class Solution:
    def __init__(self):
        self.count = 0

    def averageOfSubtree(self, root):
        self.Count(root)
        return self.count  

    def Count(self, root):
        if not root:
            return 0, 0
        lSum,lCount = self.Count(root.left)
        rSum,rCount = self.Count(root.right)

        tSum,tCount = lSum + rSum + root.val, lCount+rCount+1

        if tCount > 0:
            avg = (tSum)//tCount
            if avg == root.val:
                self.count += 1

        return tSum, tCount

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) in worst case can be O(n). h is the height and n is the no. of nodes in the given tree.

#Test Cases:
#[4,8,5,0,1,-1,6,-1,-1,-1,-1,-1,-1], [1,-1,-1]

sol = Solution()

root = tree.createBinaryTree([4,8,5,0,1,-1,6,-1,-1,-1,-1,-1,-1])
print(sol.averageOfSubtree(root))

sol.count = 0 #to flush the previous count value

root = tree.createBinaryTree([1,-1,-1])
print(sol.averageOfSubtree(root))

#Link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/