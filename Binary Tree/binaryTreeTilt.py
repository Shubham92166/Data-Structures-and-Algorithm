class Solution:
    def findTilt(self, root):
        self.sum = 0
        self.helper(root)
        return self.sum
    
    def helper(self, root):
        if not root:
            return 0
        
        leftSubTreeSum = self.helper(root.left)
        rightSubTreeSum = self.helper(root.right)
        
        self.sum += abs(leftSubTreeSum - rightSubTreeSum)
        
        return leftSubTreeSum + rightSubTreeSum +  root.val

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) in the worst case can be O(n). h is the height and n is the no. of nodes

#Test Cases:
#[1,2,3], [4,2,9,3,5,None,7], [21,7,14,1,1,2,2,3,3]

#Link: https://leetcode.com/problems/binary-tree-tilt/