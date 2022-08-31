import queue
from createBinaryTree import *

tree = BinaryTee()

def zigzagLevelOrder(root):
    if not root:
        return None

    q = queue.Queue()
    ans = []
    temp = []
    ans.append([root.val])
    q.put(root)
    q.put(None)
    level = 0
    while(not q.empty()):
        node = q.get()
        if node == None:
            if temp:
                if level%2 == 0:
                    ans.append(temp[::-1])
                else:
                    ans.append(temp)
            if not q.empty():
                q.put(None)
                temp = []
                level += 1
            continue
        if node.left:
            q.put(node.left)
            temp.append(node.left.val)
        if node.right:
            q.put(node.right)
            temp.append(node.right.val)
    return ans

#Complexity:
#Time: O(n)
#Space O(n)
#where n is the no. of nodes

#Test Cases:
#[3,9,20,null,null,15,7], [1], []

root = tree.createBinaryTree([3,9,20,None,None,15,7])
ans = zigzagLevelOrder(root)
print(ans)

root = tree.createBinaryTree([1])
ans = zigzagLevelOrder(root)
print(ans)

root = tree.createBinaryTree([])
ans = zigzagLevelOrder(root)
print(ans)

#Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/