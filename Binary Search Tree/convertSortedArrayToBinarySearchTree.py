#Approach:

#Since the given array is sorted array. We don't need to sort it. BST has the property that all the nodes in the left subtree are 
#smaller than the root and all the nodes in the right subtree. So, we will pick the middle element as the root node and recursively call
#the function for left subtree having all the elements which are before the middle element and similarly for right subtree. At the end
#we get the root of the resultant BST.

import sys
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")

from createBinaryTree import *

tree = BinaryTee()

def sortedArrayToBST(nums):
    if not nums:
        return None
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root

#Complexity:
#Time: O(n)
#Space: O(h) or log n

#Test Cases:
#[-10,-3,0,5,9,-1,-1,-1,-1,-1,-1], [1,3,-1,-1,-1]

root = sortedArrayToBST([-10,-3,0,5,9])
print(tree.printTree(root))

root = sortedArrayToBST([1,3])
print(tree.printTree(root))

#Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/