#Approach: 
#We do level order traversal on the given tree. Whenever a level ends, we append None to the queue to mark that it is the end
#of the level. When we find a valid node, we check if we have it's left and/or right child. If we have, any/both of them then add the 
#value of the child node to the total sum and increment the count. When we encounter a None which means it is the end of the leel then
#we append the sum/count to the final ans array. We do this process untill we have finished all the nodes of all levels. FInally, we 
#return the ans array.

import queue
from createBinaryTree import *

tree = BinaryTee()

def averageOfLevels(root):
    if not root:
        return None
    q = queue.Queue()
    sum = 0
    count = 0
    ans = []
    ans.append(root.val)
    q.put(root)
    q.put(None)
    while(not q.empty()):
        node = q.get()
        if not node:
            if sum and count:
                ans.append(sum/count)
            else:
                ans.append(float("{0:.5f}".format(0.00000000)))
            if not q.empty():
                q.put(None)
                sum = 0
                count = 0
            continue
        if node.left:
            q.put(node.left)
            sum += node.left.val
            count += 1
        if node.right:
            q.put(node.right)
            sum += node.right.val
            count += 1
    ans.pop()
    return ans

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[3,9,20,-1,-1,15,7, -1,-1,-1,-1], [1,1,-1,-1,-1], [3,9,20,15,7,-1,-1,-1,-1,-1,-1], [3,1,5,0,2,4,6,-1,-1,-1,-1,-1,-1,-1,-1]

root = tree.createBinaryTree([3,9,20,-1,-1,15,7, -1,-1,-1,-1])
print(averageOfLevels(root))

root = tree.createBinaryTree([3,9,20,15,7,-1,-1,-1,-1,-1,-1])
print(averageOfLevels(root))

root = tree.createBinaryTree([1,1,-1,-1,-1])
print(averageOfLevels(root))

root = tree.createBinaryTree([3,1,5,0,2,4,6,-1,-1,-1,-1,-1,-1,-1,-1])
print(averageOfLevels(root))

#Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/