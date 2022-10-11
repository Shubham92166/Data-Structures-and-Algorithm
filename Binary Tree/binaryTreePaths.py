from createBinaryTree import *

tree = BinaryTee()

class Solution:
    def binaryTreePaths(self, root):
        self.ans = []
        res = []
        temp = []

        self.helper(root, temp)
        
        for path in self.ans:
            res.append("->".join(path))
        
        return res
    
    def helper(self, root, temp):
        if not root:
            return 
        
        temp.append(root.val)
        
        if not root.left and not root.right:
            s = ""
            s = [s+str(i) for i in temp]
            self.ans.append(s)
            temp.pop()
            return 
    
        self.helper(root.left, temp)
        self.helper(root.right, temp)
        temp.pop()

#Complexity:
#Time: O(n)
#Space: O(h)
#where h in the worst case can be O(n). h is the height and n is the no. of nodes

#Test Cases:
#[1,2,3,-1,5,-1,-1,-1,-1], [1,-1,-1]

sol = Solution()

root = tree.createBinaryTree([1,2,3,-1,5,-1,-1,-1,-1])
print(sol.binaryTreePaths(root))

root = tree.createBinaryTree([1,-1,-1])
print(sol.binaryTreePaths(root))

#Link: https://leetcode.com/problems/binary-tree-paths/