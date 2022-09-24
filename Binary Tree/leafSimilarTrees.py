class Solution:
    def leafSimilar(self, root1, root2):
        self.leaves1 = []
        self.leaves2 = []
        
        self.helper(root1, True)
        self.helper(root2, False)
        
        if self.leaves1 == self.leaves2:
            return True
        
        return False
            
    def helper(self, root, flag):
        if not root:
            return 
        if not root.left and not root.right:
            if flag:
                self.leaves1.append(root.val)

            else:
                self.leaves2.append(root.val)
            return 
        
        self.helper(root.left, flag)
        self.helper(root.right, flag)

#Complexity:
#Time: O(n)
#Space: O(h)
#where in worst case O(h) can be O(n). h is the height and n is the no. of nodes

#Test Cases:
#[3,5,1,6,2,9,8,null,null,7,4], [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
#[1,2,3], [1,3,2]

#Link: https://leetcode.com/problems/leaf-similar-trees/