import queue
import math 

from createBinaryTree import *

tree = BinaryTee()

#Method-1: Using iterative approach

'''
Approach:
We do level order traversal and store the left and right subtree nodes for each level in two different arrays/list. When a level ends, 
we compare both the arrays/lists if they are same or not. If they are not then we simply return False else we will continue the process
and at the end return True.
'''

def isSymmetric1(root):
    if not root:
        return True
    left = []
    right = []
    q = queue.Queue()
    q.put(root)
    q.put(None)
    while(not q.empty()):
        node = q.get()
        if node == None:
            if left and right:
                if left != right[::-1]:
                    return False
            if not q.empty():
                q.put(None)
                left.clear()
                right.clear()
            continue
        if node.left:
            q.put(node.left)
            left.append(node.left.val)
        else:
            left.append(-math.inf)
        
        if node.right:
            q.put(node.right)
            right.append(node.right.val)
        else:
            right.append(-math.inf)
    return True

#Complexity:
#Time: O(n^2)
#Space: O(n)

root = tree.createBinaryTree([1,2,2,3,4,4,3,-1,-1,-1,-1,-1,-1,-1,-1])
print(isSymmetric1(root))

root = tree.createBinaryTree([1,2,2,-1,3,-1,3,-1,-1,-1,-1])
print(isSymmetric1(root))

#Method-2: Using Recursive approach

'''
Approach:
Since this is a mirror image. So, we can consider this as a modified version of similar trees. Here, we take left sunbtree and right 
as two different trees. If the left subtree's value is equal to right subtree's value then we call the recusion on left subtree's left 
and right subtree's right and then vice versa. If there is no node left in the both th trees then we return true else False. In case,
the value's for nodes are not same then we simply return False.
'''

def isSymmetric2(root):
    return isSymmetricHelper(root.left, root.right)
    
def isSymmetricHelper(leftTree, rightTree):
    if not leftTree and not rightTree:
        return True
    
    if not leftTree or not rightTree:
        return False
    
    if leftTree.val == rightTree.val:
        return isSymmetricHelper(leftTree.left, rightTree.right) and isSymmetricHelper(leftTree.right, rightTree.left)

    else:
        return False

#Complexity:
#Time: O(n)
#Space: O(h)
#Where n is the no. of nodes and h is the height of the tree. In worst case, O(h) is O(n)

root = tree.createBinaryTree([1,2,2,3,4,4,3,-1,-1,-1,-1,-1,-1,-1,-1])
print(isSymmetric2(root))

root = tree.createBinaryTree([1,2,2,-1,3,-1,3,-1,-1,-1,-1])
print(isSymmetric2(root))

#Test Cases:
#[1,2,2,3,4,4,3,-1,-1,-1,-1,-1,-1,-1,-1], [1,2,2,-1,3,-1,3,-1,-1,-1,-1]

#Link: https://leetcode.com/problems/symmetric-tree/
