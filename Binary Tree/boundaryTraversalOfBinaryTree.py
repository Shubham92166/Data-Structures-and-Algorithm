class Solution:
    
    def solve(self, A):
        left = self.leftTraversal(A)
        right = self.rightTraversal(A)
        
        self.leafs = []
        self.findLeaves(A)
    
        ans = [A.val]
        ans.extend(left)
        ans.extend(self.leafs)
        ans.extend(right[::-1])
        return ans

    def leftTraversal(self, A):
        left = []
        node = A.left
        while node:
            if (node.left or node.right):
                left.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
                    
        return left

    def findLeaves(self, root):
        if not root:
            return 
        
        if not root.left and not root.right:
            self.leafs.append(root.val)
        
        self.findLeaves(root.left)
        self.findLeaves(root.right)
    
    def rightTraversal(self, A):
        right = []
        node = A.right
        while node:
            if node.left or node.right:
                right.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
                    
        return right

#Complexity:
#Time: O(n)
#Space: (n)

#Link: https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1