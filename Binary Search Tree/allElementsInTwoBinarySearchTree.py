class Solution:
    def __init__(self):
        self.preOrder1 = []
        self.preOrder2 = []
        
    def getAllElements(self, root1, root2):
        self.findPreOrder(root1, True)
        self.findPreOrder(root2, False)
        
        return self.mergeTwo(self.preOrder1, self.preOrder2)
        
        
    def findPreOrder(self,  root, flag):
        if not root:
            return 
        
        self.findPreOrder(root.left, flag)
        
        if flag:
            self.preOrder1.append(root.val)
        else:
            self.preOrder2.append(root.val)
            
        self.findPreOrder(root.right, flag)
    
    def mergeTwo(self, first, second):
        i = 0
        j = 0
        ans = []
        
        while i < len(first) and j < len(second):
            if first[i] == second[j]:
                ans.append(first[i])
                ans.append(second[j])
                i += 1
                j += 1
            elif first[i] < second[j]:
                ans.append(first[i])
                i += 1
            elif second[j] < first[i]:
                ans.append(second[j])
                j += 1
        while i < len(first):
            ans.append(first[i])
            i += 1
        
        while j < len(second):
            ans.append(second[j])
            j += 1
        
        
        return ans

#Complexity:
#Time: O(m+n)
#Space: O(m+n)
#where m and n are the no. of nodes in Tree1 and Tree2 respectively

#Test Cases:
#[2,1,4], [1,0,3]
#[1,null,8], [8,1] 

#Link: https://leetcode.com/problems/all-elements-in-two-binary-search-trees/