'''
Approach: We can solve this problem if we have left subtree sum and right subtree sum by returning the sum of these two values. So, we
recursively call the function to calculate the left subtree sum and right subtree sum. If the current node doesn't have any left and 
right child then we can return the current accumulated sum. We calculate the sum as cur_sum * 10 + current node's value. We multiply by
10 here since we need to move the number to coorect value place and number's base value is 10 so we can multiply it by 10 to get the sum.
We add left subtree sum and right subtree sum and then we return the sum as the final result. If current node doesn't exist then we 
return 0
'''

from createBinaryTree import *

tree = BinaryTee()

def sumNumbers(root):
    totalSum = sum(root, 0)
    return totalSum
    
def sum(root, curSum):
    if not root:
        return 0

    curSum = curSum*10 + root.val

    if not root.left and not root.right:
        return curSum

    leftSum = sum(root.left, curSum)
    rightSum = sum(root.right, curSum)

    return leftSum + rightSum

#Complexity:
#Time: O(n)
#Space: O(h)

#Test Cases:
#[1,2,3,-1,-1,-1,-1], [4,9,0,5,1,-1,-1,-1,-1,-1,-1]

root = tree.createBinaryTree([1,2,3,-1,-1,-1,-1])
print(sumNumbers(root))

root = tree.createBinaryTree([4,9,0,5,1,-1,-1,-1,-1,-1,-1])
print(sumNumbers(root))

#Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/