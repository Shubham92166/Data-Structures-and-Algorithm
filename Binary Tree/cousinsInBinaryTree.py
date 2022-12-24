from createBinaryTree import *

tree = BinaryTee()

#Method-1: Using DFS (2 passes):

'''
Approach:
To check whether they are cousins are not. They should be in the generation and their parents should't be same. So, for the given nodes
we find the parent and level recursively and check if there parents are different and generation(level) is same. If the above condition
satisfy then they are cousins so we return True else they are not cousins so we return False
'''

def isCousins1(root, x, y):
    dummy = TreeNode(-1)

    levelOfX, parentOfX = searchNode(root, x, dummy, 0)
    levelOfY, parentOfY = searchNode(root, y, dummy, 0)

    if levelOfX == levelOfY and parentOfX != parentOfY:
        return True
    else:
        return False
    
def searchNode(root, value, parent, level):
    if not root:
        return ()

    if root.val == value:
        return (level, parent.val)

    left = searchNode(root.left, value, root, level+1)
    right = searchNode(root.right, value, root, level+1)

    return left or right

#Complexity:
#Time: O(n)
#Space: O(h)
#where h in worst case can be n. h is the height and n is the no. of nodes

root = tree.createBinaryTree([1,2,3,4,-1,-1,-1,-1,-1])
print(isCousins1(root, 4, 3))

root = tree.createBinaryTree([1,2,3,-1,4,-1,5,-1,-1,-1,-1])
print(isCousins1(root, 5, 4))

root = tree.createBinaryTree([1,2,3,-1,4,-1,-1,-1,-1])
print(isCousins1(root, 2, 3))

#Method-2: Using DFS (1 pass):

'''
Approach:
The approach is same as Method-1. However, in Method-1 we were calling two recursive functions. One for each node. This can be done in a 
single call and thus improving the code readability and code will run faster.
So, in this method, we will return 4 values only if there parents are not same else we will return only two paraments. Now, there is an
edge case, if there parents are different but their generations are also different that means they are not cousins. So, to handle this 
case, we are still checking the conditions as in Method-1.
'''

def isCousins2(root, x, y):
    dummy = TreeNode(-1)
    ans = searchNode(root, x, dummy, y, dummy, 0)
    if len(ans) != 4:
        return False
    levelOfX, parentOfX, levelOfY, parentOfY = ans
    if levelOfX == levelOfY and parentOfX != parentOfY:
        return True
    else:
        return False
    
def searchNode(root, value1, parent1, value2, parent2, level):
    if not root:
        return ()
    if root.val == value1:
        return [level, parent1.val]
    
    if root.val == value2:
        return [level, parent2.val]
    
    left = searchNode(root.left, value1, root, value2, root, level+1)
    right = searchNode(root.right, value1, root, value2, root, level+1)
    ans = []
    if left:
        ans.extend(left)
    if right:
        ans.extend(right)
    
    return ans

#Complexity:
#Time: O(n)
#Space: O(h)
#where h in worst case can be n. h is the height and n is the no. of nodes

#Test Cases:
#[1,2,3,4,-1,-1,-1,-1,-1], 4, 3
#[1,2,3,-1,4,-1,5,-1,-1,-1,-1], 5, 4
#[1,2,3,-1,4,-1,-1,-1,-1], 2, 3

root = tree.createBinaryTree([1,2,3,4,-1,-1,-1,-1,-1])
print(isCousins2(root, 4, 3))

root = tree.createBinaryTree([1,2,3,-1,4,-1,5,-1,-1,-1,-1])
print(isCousins2(root, 5, 4))

root = tree.createBinaryTree([1,2,3,-1,4,-1,-1,-1,-1])
print(isCousins2(root, 2, 3))

#Link: https://leetcode.com/problems/cousins-in-binary-tree/