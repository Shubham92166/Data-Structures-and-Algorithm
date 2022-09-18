class Solution:
    def __init__(self):
        self.dic = {}
    def reverseOddLevels(self, root):
        self.Traverse(root, 0)
        self.reverseLevel(root, 0)
        return root
    
    def Traverse(self, root, level):
        if not root:
            return 
        
        if level % 2 != 0:
            if level in self.dic:
                values = self.dic.get(level)
                values.append(root.val)
                self.dic[level] = values
            else:
                values = [root.val]
                self.dic[level] = values
        
        self.Traverse(root.left, level + 1)
        self.Traverse(root.right, level + 1)
    
    def reverseLevel(self, root, level):
        if not root:
            return 
        
        if level % 2 != 0:
            values = self.dic.get(level)
            root.val = values.pop()
        
        self.reverseLevel(root.left, level + 1)
        self.reverseLevel(root.right, level + 1)

#Complexity:
#Time: O(n)
#Space: O(h)
#where h is the height and n is the no. of nodes

#Test Cases:
#[2,3,5,8,13,21,34], [7,13,11], [0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]

#Link: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/