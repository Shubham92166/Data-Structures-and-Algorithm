import queue
from createBinaryTree import *

tree = BinaryTee()

def levelOrderBottom(root):
    if not root:
        return None
    q = queue.Queue()
    res = []
    res.append([root.val])
    temp = []
    q.put(root)
    q.put(None)
    while(not q.empty()):
        node = q.get()
        if node == None:
            if temp:
                res.append(temp)
            if not q.empty():
                q.put(None)
                temp = []
            continue
        if node.left:
            q.put(node.left)
            temp.append(node.left.val)
        if node.right:
            q.put(node.right)
            temp.append(node.right.val)
    return res[::-1]

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the no. of nodes

#Test Cases:
#[3,9,20,-1,-1,15,7,-1,-1,-1,-1], [1,-1,-1], []

root = tree.createBinaryTree([3,9,20,-1,-1,15,7,-1,-1,-1,-1])
print(levelOrderBottom(root))

root = tree.createBinaryTree([1,-1,-1])
print(levelOrderBottom(root))

root = tree.createBinaryTree([])
print(levelOrderBottom(root))

#Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/