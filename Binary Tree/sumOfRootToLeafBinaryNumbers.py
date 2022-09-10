from createBinaryTree import *

tree = BinaryTee()

def sumRootToLeaf(root):
        sum = 0
        return helper(root, sum)
    
def helper(root, sum):
    if not root:
        return 0
    
    sum = (2*sum) + root.val
    
    if not root.left and not root.right:
        return sum
    
    return helper(root.left, sum) + helper(root.right, sum)

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1,0,1,0,1,0,1], [0]

#root = tree.createBinaryTree([1,0,1,0,1,0,1])
#print(sumRootToLeaf(root))

#root = tree.createBinaryTree([0])
#print(sumRootToLeaf(root))

#Link: https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/



