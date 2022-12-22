'''
Approach: 
We call the recursive function on both the trees, if both the nodes have left child and/or right child and their values are 
same then we keep calling and checking it for rest of the nodes. If any of the above condition fails then we simply return False as both
the trees are not same.
'''

from createBinaryTree import *

tree = BinaryTee()

def isSameTree(p, q):
    if not p and not q:
        return True
    
    if (p and not q) or (not p and q) or (p.val != q.val):
        return False

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

#Complexity:
#Time: O(n)
#Space: O(h)
#Where n is the no. of nodes and h is the height of the tree. In worst case, O(h) can be O(n).

#Test Cases:
#[1,2,3,-1,-1,-1,-1], [1,2,3,-1,-1,-1,-1]
#[1,2,-1,-1,-1], [1,-1,2,-1,-1]
#[1,2,1,-1,-1,-1,-1], [1,1,2,-1,-1,-1,-1]

root1 = tree.createBinaryTree([1,2,3,-1,-1,-1,-1])
root2 = tree.createBinaryTree([1,2,3,-1,-1,-1,-1])
print(isSameTree(root1, root2))

root1 = tree.createBinaryTree([1,2,-1,-1,-1])
root2 = tree.createBinaryTree([1,-1,2,-1,-1])
print(isSameTree(root1, root2))

root1 = tree.createBinaryTree([1,2,1,-1,-1,-1,-1])
root2 = tree.createBinaryTree([1,1,2,-1,-1,-1,-1])
print(isSameTree(root1, root2))

#Link: https://leetcode.com/problems/same-tree/
