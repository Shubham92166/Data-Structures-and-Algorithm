from createBinaryTree import *

tree = BinaryTee()

def addOneRow(root, val, depth):
    if not root:
        return None
    level = 1
    if depth == 1:
        leftSubTree = root
        root = TreeNode(val)
        root.left = leftSubTree
        return root

    addRow(root, level, val, depth)
    return root

def addRow(root, level, val, depth):
    if not root:
            return None

    if level == depth-1:
        leftSubTree = root.left
        root.left = TreeNode(val)
        root.left.left = leftSubTree

        rightSubTree = root.right
        root.right = TreeNode(val)
        root.right.right = rightSubTree
        
    addRow(root.left, level + 1, val, depth)
    addRow(root.right, level + 1, val, depth)

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) in worst case can be O(n). h is the height and n is the no. of nodes

#Test Cases:
#[4,2,6,3,1,5, -1, -1, -1, -1, -1, -1, -1], 1, 2
#[4,2,-1,3,1,-1,-1,-1,-1], 1, 3

root = tree.createBinaryTree([4,2,6,3,1,5, -1, -1, -1, -1, -1, -1, -1])
root = addOneRow(root, 1, 2)
print(tree.printTree(root))

root = tree.createBinaryTree([4,2,-1,3,1,-1,-1,-1,-1])
root = addOneRow(root, 1, 3) 
print(tree.printTree(root))  
        
#Link: https://leetcode.com/problems/add-one-row-to-tree/