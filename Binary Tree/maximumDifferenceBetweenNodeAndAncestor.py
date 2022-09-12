import math 
from createBinaryTree import *

def maxAncestorDiff(root):
    minNode = math.inf
    maxNode = -math.inf
    
    return helper(root, minNode, maxNode)
    

def helper(root, minNode, maxNode):
    if not root:
        return maxNode - minNode
    
    minNode = min(minNode, root.val)
    maxNode = max(maxNode, root.val)
    
    return max(helper(root.left, minNode, maxNode), helper(root.right, minNode, maxNode))

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) in worst case can be O(n). h is the height and n is the no. of nodes

#Test Cases:
#[8,3,10,1,6,None,14,None,None,4,7,13], [1,None,2,None,0,3]

#Link: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/