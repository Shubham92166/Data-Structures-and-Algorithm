import sys
sys.path.insert(1, "C:\\Users\\Dell\\Desktop\DSA Hands-on\\Data-Structures-and-Algorithms\\Data-Structures-and-Algorithm\\Binary Tree")

from createBinaryTree import *

tree = BinaryTee()

class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.third = None
        self.prev = None

    def recoverTree(self, root):
        self.helper(root)

        if self.third and self.first:
            self.first.val, self.third.val = self.third.val, self.first.val
        elif self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val 
        
        return root
        

    def helper(self, root): 
        if not root:
            return 
        
        self.helper(root.left)

        if self.prev != None and root.val < self.prev.val:
            if self.first == None:
                self.first = self.prev
                self.second = root
            else:
                self.third = root
        
        self.prev = root
        self.helper(root.right)

#Complexity:
#Time: O(n)
#Space: O(1)
#Where n is the no. of nodes

#Test Cases:
#[1,3,-1,-1,2,-1,-1], [3,1,4,-1,-1,2,-1,-1,-1]

sol = Solution()
root = tree.createBinaryTree([1,3,-1,-1,2,-1,-1])
newRoot = sol.recoverTree(root)
print(tree.printTree(newRoot))

sol = Solution()
root = tree.createBinaryTree([3,1,4,-1,-1,2,-1,-1,-1])
newRoot = sol.recoverTree(root)
print(tree.printTree(newRoot))

#Link: https://leetcode.com/problems/recover-binary-search-tree/

