class Solution:
    def pathSum(self, root, targetSum):
        self.ans = []
        temp = []
        sum = 0
        self.helper(root, targetSum, sum, temp, self.ans)
        return self.ans

    def helper(self, root, target, sum, temp, ans):
        if not root:
            return 0
        
        sum += root.val
        temp.append(root.val)
        
        if not root.left and not root.right:
            if sum == target:
                self.ans.append(temp.copy())
            sum -= root.val
            temp.pop()
            return
        
        self.helper(root.left, target, sum, temp, ans)
        self.helper(root.right, target, sum, temp, ans)
        temp.pop()

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) in worst case can be O(n) and h is height and n is the no. of nodes

#Test Cases:
#[5,4,8,11,null,13,4,7,2,null,null,5,1], 22
#[1,2,3], 5
#[1,2], 0

#Link: https://leetcode.com/problems/path-sum-ii/

