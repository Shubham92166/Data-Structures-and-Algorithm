''''
Approach: The find minimum no. of swaps at each level, we need to store the nodes at each level. So, we are doing BFS traversal and 
storing teh nodes at each level in a temporary array. Once all the nodes are stored in the temporary array, we are calling another 
method to find the minimum no. of swaps. 
To find minimum no. of swaps, we first store each element as a pair with its index in an another temporary array and sort it by its
value. Now, if we check the elements are their correct position. If they aren't then we swap with the pair of correct position. By doing
so, at each iteration, one pair comes at its correct position. In this way, we count the no. of swaps at each level. We add the no. of 
swaps of all levels and return it as the final answer.
'''

from createBinaryTree import *

tree = BinaryTee()

import queue

def minimumOperations(root):
    if not root:
        return 0
    q = queue.Queue()
    q.put(root)
    q.put(None)
    temp = []
    levels = []
    swaps = 0
    while not q.empty():
        node = q.get()
        if not node:
            if not q.empty():
                if temp:
                    swaps += compare(temp)
                q.put(None)
                temp = []
            continue
        
        if node.left:
            q.put(node.left)
            temp.append(node.left.val)
        
        if node.right:
            q.put(node.right)
            temp.append(node.right.val)
            
    return swaps
            
def compare(A):
    l = []
    n = len(A)
    for i in range(n):
        l.append((A[i], i))

    l.sort(key = lambda x: x[0])

    swaps = 0
    index = 0

    while index < n:
        if index == l[index][1]:
            index += 1
        else:
            temp = l[index][1]
            l[index], l[temp] = l[temp], l[index]
            swaps += 1
        
    return swaps

#Complexity:
#Time: O(nlog n)
#Space: O(n)

#Test Cases:
#[1,3,2,7,6,5,4,-1,-1,-1,-1,-1,-1,-1,-1], [1,2,3,4,5,6,-1,-1,-1,-1,-1,-1,-1], [1,4,3,7,6,8,5,-1,-1,-1,-1,9,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1]

root = tree.createBinaryTree([1,3,2,7,6,5,4,-1,-1,-1,-1,-1,-1,-1,-1])
print(minimumOperations(root))

root = tree.createBinaryTree([1,2,3,4,5,6,-1,-1,-1,-1,-1,-1,-1])
print(minimumOperations(root))

root = tree.createBinaryTree([1,4,3,7,6,8,5,-1,-1,-1,-1,9,-1,10,-1,-1,-1,-1,-1,-1,-1,-1,-1])
print(minimumOperations(root))

#Link: https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/