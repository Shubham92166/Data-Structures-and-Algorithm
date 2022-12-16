from createBinaryTree import *

tree = BinaryTee()

class Solution:
    def __init__(self):
        self.path = []
        self.ans = []

    def distanceK(self, root, target, k):
        if not root:
            return
       
        self.findSourcePath(root, target)
        self.findAllNodes(root, k)
       
        return self.ans
    
    def findSourcePath(self, root, target):
        if not root:
            return False
        
        if root.val == target:
            self.path.append(root)
            return True
        
        left = self.findSourcePath(root.left, target)
        right = self.findSourcePath(root.right, target)

        if left or right:
            self.path.append(root)
            return True

        return False
        
    
    def findAllNodes(self, root, k):
        self.ans = self.findNodesHelper(self.path[0], k, [])
        k -= 1

        for index in range(1, len(self.path)):
            if k == 0:
                self.ans.append(self.path[index].val)
                break

            if self.path[index].left == self.path[index-1]: 
                allNodes = self.findNodesHelper(self.path[index].right, k-1, [])
            
            else:
                allNodes = self.findNodesHelper(self.path[index].left, k-1, [])
            
            k -= 1
            
            if allNodes:
                self.ans.extend(allNodes)
        
        return self.ans
    
    def findNodesHelper(self, root, k, nodes):
        if not root:
            return 
        
        if k == 0:
            nodes.append(root.val)

        self.findNodesHelper(root.left, k-1, nodes)
        self.findNodesHelper(root.right, k-1, nodes)
        return nodes
    
#Complexity:
#Time: O(n)
#Space: O(h)
#Where n is the no. of nodes and h is the height of the tree. O(h) can be O(n) in the worst case

#Test Cases:
#[3,5,1,6,2,0,8,-1,-1,7,4,-1,-1,-1,-1,-1,-1,-1,-1], 5, 2
#[1,-1,-1], 1, 3

sol = Solution()

root = tree.createBinaryTree([3,5,1,6,2,0,8,-1,-1,7,4,-1,-1,-1,-1,-1,-1,-1,-1])
print(sol.distanceK(root, 5, 2))

sol = Solution()

root = tree.createBinaryTree([1,-1,-1])
print(sol.distanceK(root, 1, 3))

#Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/



