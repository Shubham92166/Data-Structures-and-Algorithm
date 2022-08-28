#Method 1: Using Iteration

class Solution:
    def __init__(self):
        self.ans = []
        self.stack = []
    def postorderTraversal(self, root):
        cur = root
        while cur or self.stack:
            if cur:
                self.stack.append(cur)
                cur = cur.left
            else:
                temp = self.stack[-1].right
                if not temp:
                    temp = self.stack[-1]
                    self.stack.pop()
                    self.ans.append(temp.val)
                    while self.stack and temp == self.stack[-1].right:
                        temp = self.stack[-1]
                        self.stack.pop()
                        self.ans.append(temp.val)
                else:
                    cur = temp
        return self.ans
    
#Complexity:
#Time: O(n)
#Space: O(1) #if we ignore the space required for storing the ans
#where n is the no. of nodes

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
#Time: O(n)
#Space: O(n)
#where n is the no. of nodes

#Test Cases:
#[1,null,2,3], [], [1]

#Link: https://leetcode.com/problems/binary-tree-postorder-traversal/