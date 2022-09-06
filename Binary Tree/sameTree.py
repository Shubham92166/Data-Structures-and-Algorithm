from createBinaryTree import *

tree = BinaryTee()

def isSameTree(p, q):
    if not p and q or p and not q:
        return False
    if not p and not q:
        return True
    if p.val != q.val:
        return False
    res1  = isSameTree(p.left, q.left)
    res2 = isSameTree(p.right, q.right)
    return res1 and res2

#Complexity:
#Time: O(H)
#Space: O(H)
#where O(H) can be O(n) in worst case and n is the no. of nodes

#Test Cases:
#[1,2,3], [1,2,3]
#[1,2], [1,None,2]
#[1,2,1], [1,1,2]

root1 = tree.createBinaryTree([1,2,3])
root2 = tree.createBinaryTree([1,2,3])
print(isSameTree(root1, root2))

root1 = tree.createBinaryTree([1,2])
root2 = tree.createBinaryTree([1,None,2])
print(isSameTree(root1, root2))

root1 = tree.createBinaryTree([1,2,1])
root2 = tree.createBinaryTree([1,1,2])
print(isSameTree(root1, root2))

#Link: https://leetcode.com/problems/same-tree/
