'''
Approach: We do DFS traversal on both the trees and update the value of tree1 root's value as tree1 root's value + tree2 root's value.
'''

from createBinaryTree import *

tree = BinaryTee()

def mergeTrees(root1, root2):
    if not root1 and not root2:
        return None

    elif not root1:
        return root2

    elif not root2:
        return root1

    root1.val += root2.val

    root1.left = mergeTrees(root1.left, root2.left)
    root1.right = mergeTrees(root1.right, root2.right)
    
    return root1

#Complexity:
#Time: O(h1+h2)
#Space: O(h1+h2)
#Where h1 is the height of tree1 and h2 is the height of tree2

#Test Cases:
#[1,3,2,5,-1,-1,-1,-1,-1], [2,1,3,-1,4,-1,7,-1,-1,-1,-1,-1,-1]
#[1,-1,-1], [1,2,-1,-1,-1]

root1 = tree.createBinaryTree([1,3,2,5,-1,-1,-1,-1,-1])
root2 = tree.createBinaryTree([2,1,3,-1,4,-1,7,-1,-1,-1,-1,-1,-1])
print(tree.printTree(mergeTrees(root1, root2)))

root1 = tree.createBinaryTree([1,-1,-1])
root2 = tree.createBinaryTree([1,2,-1,-1,-1])
print(tree.printTree(mergeTrees(root1, root2)))

#Link: https://leetcode.com/problems/merge-two-binary-trees/