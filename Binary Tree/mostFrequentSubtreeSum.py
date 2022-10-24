from createBinaryTree import *

tree = BinaryTee()

class Solution:
    def findFrequentTreeSum(self, root):
        self.dic = {}
        self.helper(root)
        ans = []
        maxFreq = max(self.dic.values())
        for key, val in self.dic.items():
            if val == maxFreq:
                ans.append(key)
        
        return ans

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        sum = left+right+root.val
        if sum not in self.dic:
            self.dic[sum] = 1
        else:
            self.dic[sum] += 1
        return sum

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[5,2,-3], [5,2,-5]

sol = Solution()

root = tree.createBinaryTree([5,2,-3])
print(sol.findFrequentTreeSum(root))

root = tree.createBinaryTree([5,2,-5])
print(sol.findFrequentTreeSum(root))

#Link: https://leetcode.com/problems/most-frequent-subtree-sum/
