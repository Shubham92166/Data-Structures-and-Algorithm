'''
Approach: 
In order to findthe sum of all nodes having even valued grandparent is we need to maintain the grandparant so to do so we will
pass the grandparent as a parameter while making the recursive call. However, we also need to maintain parent because a parent node is a
grandparent node. So, we will pass both nodes as argumuments in the recursion call. Since root node doesn't have any parent or grandpar-
ent node so we will pass dummy nodes. While calling for left child and right child, the current node will become the parent the parent 
of current node will become the grandparent. While traversing, we check if the grandparent has even value. If yes then we add current 
node's value to the total sum and at the end we return it.
'''

from createBinaryTree import *

tree = BinaryTee()

class Solution:
    def __init__(self):
        self.sum = 0
        
    def sumEvenGrandparent(self, root):
        dummy = TreeNode(-1)
        self.Sum(root, dummy, dummy)
        return self.sum
    
    def Sum(self, root, gp, p):
        if not root:
            return
        
        if gp.val % 2 == 0:
            self.sum += root.val
        
        self.Sum(root.left, p, root)
        self.Sum(root.right, p, root)

#Complexity:
#Time: O(n)
#Space: O(h)
#Where h is the height and n is the no. of nodes. O(h) in worst case can be O(n). 

#Test Cases:
#[6,7,8,2,7,1,3,9,-1,1,4,-1,-1,-1,5,-1,-1,-1,-1,-1,-1,-1,-1]

sol = Solution()

root = tree.createBinaryTree([6,7,8,2,7,1,3,9,-1,1,4,-1,-1,-1,5,-1,-1,-1,-1,-1,-1,-1,-1])
print(sol.sumEvenGrandparent(root))

#Link: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/