from createBinaryTree import *

class Solution:
    def __init__(self):
        self.pathOfp = []
        self.pathOfq = []

    def lowestCommonAncestor(self, root, p, q):
        
        self.findPath(root, p.val, True)
        self.findPath(root, q.val, False)

        self.pathOfp =  self.pathOfp[::-1]
        
        if not self.pathOfp and self.pathOfq:
            return self.pathOfq[0]
        
        elif self.pathOfp and not self.pathOfq:
            return self.pathOfp[0]
        
        else:
            prev = TreeNode(-1)
            i = 0
            j = len(self.pathOfq)-1
            while i < len(self.pathOfp) and j >= 0 and self.pathOfp[i] == self.pathOfq[j]:
                prev = self.pathOfp[i]
                i += 1
                j -= 1
            return prev
    
    def findPath(self, root, node, flag):
        if not root:
            return False
        
        if root.val == node:
            if flag:
                self.pathOfp.append(root)
            else:
                self.pathOfq.append(root)
            return True
       
        
        left = self.findPath(root.left, node, flag) 
        right = self.findPath(root.right, node, flag)
        
        if left or right:
            if flag:
                self.pathOfp.append(root)
            else:
                self.pathOfq.append(root)
            return True
        
        return False

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) in worst case can be O(n). h is the height and n is the no. of nodes

#Test Cases:
#[3,5,1,6,2,0,8,None,None,7,4], 5, 1
#[3,5,1,6,2,0,8,None,None,7,4], 5, 4
#[1,2], 1, 2
#[1,2,3,None,5], 3, 5
#[1,2,5,3,4,None,6], 1, 6
#[1,2,5,3,4,None,6], 2, 6

#Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/