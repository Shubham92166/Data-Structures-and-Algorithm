#Method 1: Using Iteration
from createBinaryTree import *
tree = BinaryTee()
        
def postorderTraversal(root):
    cur = root
    ans = []
    stack = []
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            temp = stack[-1].right
            if not temp:
                temp = stack[-1]
                stack.pop()
                ans.append(temp.val)
                while stack and temp == stack[-1].right:
                    temp = stack[-1]
                    stack.pop()
                    ans.append(temp.val)
            else:
                cur = temp
    return ans
    
#Complexity:
#Time: O(n)
#Space: O(n) 
#where n is the no. of nodes

#Run:

root = tree.createBinaryTree([1,-1, 2, 3, -1, -1, -1])
print(postorderTraversal(root))

root = tree.createBinaryTree([1,-1, -1])
print(postorderTraversal(root)) 

root = tree.createBinaryTree([])
print(postorderTraversal(root)) 

#Method 2: Using Recursion

def postorderTraversal(root):
        ans = []
        postOrder(root, ans)
        return ans

def postOrder(root, ans):
    if not root:
        return None
    
    postOrder(root.left, ans)
    postOrder(root.right, ans)
    ans.append(root.val)


#Complexity:
#Time: O(n^2)
#Space: O(n)
#where n is the no. of nodes

#Test Cases:
#[1,-1, -1]
#[1,-1, 2, 3, -1, -1, -1]
#[]

#Run:

root = tree.createBinaryTree([1,-1, 2, 3, -1, -1, -1])
print(postorderTraversal(root)) 

root = tree.createBinaryTree([1,-1, -1])
print(postorderTraversal(root)) 

root = tree.createBinaryTree([])
print(postorderTraversal(root)) 

#Link: https://leetcode.com/problems/binary-tree-postorder-traversal/