from createBinaryTree import *

tree = BinaryTee()

def invertTree(root):
    if not root:
        return None
    leftTree = root.left
    root.left = root.right
    root.right = leftTree

    invertTree(root.left)
    invertTree(root.right)

    return root

#Complexity:
#Time: O(n)
#Space: O(H)
#where O(H) in worst case can be O(n)

#Test Cases
#[4,2,7,1,3,6,9], [2,1,3], []

root = tree.createBinaryTree([4,2,7,1,3,6,9])
root = invertTree(root)
print(tree.printTree(root))

root = tree.createBinaryTree([2,1,3])
root = invertTree(root)
print(tree.printTree(root))

root = tree.createBinaryTree([])
root = invertTree(root)
print(tree.printTree(root))

#Link: https://leetcode.com/problems/invert-binary-tree/
