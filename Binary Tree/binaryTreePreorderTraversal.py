from createBinaryTree import *

tree = BinaryTee()

def preorderTraversal(root):
        ans = []
        preOrder(root, ans)
        return ans
def preOrder(root, ans):
    if not root:
        return []
    ans.append(root.val)
    preOrder(root.left, ans)
    preOrder(root.right, ans)

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the no. of nodes

#Test Cases:
#[1,null,2,3], [], [1]

root = tree.createBinaryTree([1,None,2,3])
print(tree.printTree(root))
print(preorderTraversal(root))

#Link: https://leetcode.com/problems/binary-tree-preorder-traversal/