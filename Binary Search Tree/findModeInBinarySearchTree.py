class Solution:
    def __init__(self):
        self.dic = {}
    def findMode(self, root):
        self.helper(root)
        ans = []
        maxValue = max(self.dic.values())
        for key, val in self.dic.items():
            if val == maxValue:
                ans.append(key)
        return ans
    
    def helper(self, root):
        if not root:
            return True
        
        self.dic[root.val] = self.dic.get(root.val, 0) + 1
        self.helper(root.left) 
        self.helper(root.right)

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1,null,2,2], [0], [1,null,2]

#Link: https://leetcode.com/problems/find-mode-in-binary-search-tree/