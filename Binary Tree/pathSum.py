'''
Approach:

We will do DFS traversal on the given tree. Initially we take current sum as 0. While ttraversing, we will add nodes's value to our 
current sum if that node is non leaf node. If the node is a leaf node then we check if the current sum is equals to the given target.
If it is equal then we return True. Else we subtract the current node's value from the current sum and return False. We do this process
for left subtree and right subtree.
'''

from createBinaryTree import *

tree = BinaryTee()

def hasPathSum(root, targetSum):
    if not root:
        return False
    return checkPath(root, 0, targetSum)

def checkPath(root, sum, targetSum):
    if not root:
        return False

    sum += root.val

    if not root.left and not root.right:
        if sum == targetSum:
            return True

        sum -= root.val
        return False

    leftCheck = checkPath(root.left, sum, targetSum)
    rightCheck = checkPath(root.right, sum, targetSum)

    return leftCheck or rightCheck

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) can be O(n) in worst case. h is the height and n is the no. of nodes

#Test Cases:
#[5,4,8,11,-1,13,4,7,2,-1,-1,-1,1,-1,-1,-1,-1,-1,-1], 22
#[1,2,3,-1,-1,-1,-1], 5

root = tree.createBinaryTree([5,4,8,11,-1,13,4,7,2,-1,-1,-1,1,-1,-1,-1,-1,-1,-1])
print(hasPathSum(root, 22))

root = tree.createBinaryTree([1,2,3,-1,-1,-1,-1])
print(hasPathSum(root, 5))

#Link: https://leetcode.com/problems/path-sum/