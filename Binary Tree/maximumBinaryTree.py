'''
Approach: 

To create a maximum tree, we create the root node with maximum value of the array. We find the maximum value's index. All the nodes 
which are before the maximum node will come on left subtree and all the nodes which come after the maximum node will come on the right
subtree. We call the recursive method on both left subtree and right subtree. At the end, we return the root of the tree.
'''

from createBinaryTree import *

tree = BinaryTee()

def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    
    rootVal = max(nums)
    root = TreeNode(rootVal)
    index = nums.index(rootVal)
    
    root.left = constructMaximumBinaryTree(nums[:index])
    root.right = constructMaximumBinaryTree(nums[index+1:])

    return root

#Complexity:
#Time: O(n^2)
#Space: O(h)
#Where O(h) can be O(n). h is the height and n is the number of nodes 

#Test Cases:
#[3,2,1,6,0,5], [3,2,1]

#Link: https://leetcode.com/problems/maximum-binary-tree/
    