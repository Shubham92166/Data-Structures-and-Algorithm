import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.root = None

    def solve(self, A):
        self.constructTree(A)
        ans = []
        self.preOrder(self.root, ans)
        
        for i in range(1, len(ans)-1):
            if ans[i-1] > ans[i]:
                return "NO"
        return "YES"

    def constructTree(self, A):
        for i in A:
            if not self.root:
                self.root = Node(i) 
                root = self.root
            
            if i > root.val:
                root.right = Node(i)
                root = root.right
            else:
                root.left = Node(i)
                root = root.left
    
        
    def preOrder(self, root, ans):
        if not root:
            return 
        
        self.preOrder(root.left, ans)
        ans.append(root.val)
        self.preOrder(root.right, ans)

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[4, 10, 5, 8], [1, 5, 6, 4]

