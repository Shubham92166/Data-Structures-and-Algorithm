#Method-1: By storing each level nodes and reversing the array based on level

'''
Approach:
We do the level order traversal and while traversing we maintain a variable called level which indiates the current level at which we 
are and we also maintain an ans array that we need to return. Whenever a level ends then we check if the current level that ended now 
was a odd level or even level. If it was an odd level then before appending it to ans array we reverse it and then append else we 
directly append it to ans array and finally we increment the level variable to indicate the start of new level. At the end of whole tree
traversal, we return the ans array.
'''

import queue
from createBinaryTree import *

tree = BinaryTee()

def zigzagLevelOrder1(root):
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
#Where n is the no. of nodes

root = tree.createBinaryTree([3,9,20,-1,-1,15,7,-1,-1,-1,-1])
print(zigzagLevelOrder1(root))

root = tree.createBinaryTree([1,-1,-1])
print(zigzagLevelOrder1(root))

root = tree.createBinaryTree([-1])
print(zigzagLevelOrder1(root))

#Method-2: Optimized approach using stack and no need to reverse the array before storing

'''
Approach:
We take two stacks let's say stack1 and stack2 and maintain ans array to store the nodes for each level which we need to return. 
Initially we push the root node of the tree to the first stack. Then we do following until both the stacks do not become empty.

We maintain a temporary array to store the node's value for each level.

1. While stack1 is not empty, we do following steps:
a) We pop the node from the stack1 and check if it's left and/or right child exist
b) If they exist then we push them to stack2 [first left child and then right child]

We check if there is some elements in temp array, basically to check if temp array is not empty. If it is not empty then we append it to
ans array. 

Similarly, we do for stack2

We maintain a temporary array to store the node's value for each level.

1. While stack2 is not empty, we do following steps:
a) We pop the node from the stack1 and check if it's left and/or right child exist
b) If they exist then we push them to stack1 [first right child and then left child]

Again, We check if there is some elements in temp array, basically to check if temp array is not empty. If it is not empty then we 
append it to ans array.

Finally, we return ans array.
'''

def zigzagLevelOrder2(root):
    ans = []
    stack1 = []
    stack2 = []

    if not root:
        return 
    
    stack1.append(root)

    while stack1 or stack2:
        temp = []
        while stack1:
            node = stack1.pop()

            temp.append(node.val)

            if node.left:
                stack2.append(node.left)
            
            if node.right:
                stack2.append(node.right)
        
        if temp:
            ans.append(temp)

        temp = []

        while stack2:
            node = stack2.pop()
            temp.append(node.val)

            if node.right:
                stack1.append(node.right)

            if node.left:
                stack1.append(node.left)

        if temp:
            ans.append(temp)

    return ans

root = tree.createBinaryTree([3,9,20,-1,-1,15,7,-1,-1,-1,-1])
print(zigzagLevelOrder2(root))

root = tree.createBinaryTree([1,-1,-1])
print(zigzagLevelOrder2(root))

root = tree.createBinaryTree([-1])
print(zigzagLevelOrder2(root))

#Complexity:
#Time: O(n)
#Space O(n)
#Where n is the no. of nodes

#Test Cases:
#[3,9,20,-1,-1,15,7,-1,-1,-1,-1], [1,-1,-1], [-1]

#Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/