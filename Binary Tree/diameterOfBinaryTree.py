from createBinaryTree import BinaryTee

tree = BinaryTee()
class Solution:
    def __init__(self):
        self.ans = -1

    def diameterOfBinaryTree(self, root):
        self.height(root)
        return self.ans
    
    def height(self, root):
        if not root:
            return -1
        
        lh = self.height(root.left)
        rh = self.height(root.right)
        self.ans = max(self.ans, lh + rh + 2)
        
        return max(lh, rh) + 1

#Complexity:
#Time: O(n)
#Space: O(h)
#where in worst case O(h) can be O(n)

#Test Cases:
#[1,2,3,4,5], [1,2]

sol = Solution()

root1 = tree.createBinaryTree([1,2,3,4,5])
print(sol.diameterOfBinaryTree(root1))

#Link: https://leetcode.com/problems/diameter-of-binary-tree/