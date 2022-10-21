#Approach: 
#We take a queue to store the nodes. We initially push the root of the tree to queue and None value to mark the end of the 
#level. We pop from the queue until the queue is not empty. for each node whether we have it left and/or right child. If we have then
#append it's value to a temporary array which stores the node levelwise. If we find a None value means the level has ended. In this case,
#we append the tempory aaray to the final answer array which stores the nodes for all levels. We then check if the queue is not empty.
#If it is not empty then we push None to queue to mark the end of the current level and flush the temporary array. At the end, we return
#the final answer array.

import queue

from createBinaryTree import *

tree = BinaryTee()

def levelOrder(root):
    if not root:
        return None
    ans = []
    temp = []
    ans.append([root.val])
    q = queue.Queue()
    q.put(root)
    q.put(None)
    while(not q.empty()):
        node = q.get()
        if node == None:
            if temp:
                ans.append(temp)
                
            if not q.empty():
                q.put(None)
                temp = []
            continue
        
        if node.left:
            temp.append(node.left.val)
            q.put(node.left)
        if node.right:
            temp.append(node.right.val)
            q.put(node.right)
    return ans

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the no. of nodes

#Test Cases:
#[3,9,20,-1,-1,15,7,-1,-1,-1,-1], [1,-1,-1], []

root = tree.createBinaryTree([3,9,20,-1,-1,15,7,-1,-1,-1,-1])
print(levelOrder(root))

root = tree.createBinaryTree([1,-1,-1])
print(levelOrder(root))

root = tree.createBinaryTree([])
print(levelOrder(root))

#Link: https://leetcode.com/problems/binary-tree-level-order-traversal/