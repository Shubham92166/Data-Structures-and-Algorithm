from sys import setrecursionlimit
setrecursionlimit(10**8)
class Solution:
    def solve(self, A, B, C):
        dp = [[None for j in range(C+1)] for i in range(len(A))]
        return self.helper(A, B, C, 0, len(A), dp, 0)
        
    def helper(self, A, B, C, i, n, dp, valSum):
        if i == n:
           return 0
         
        if dp[i][C] != None:
            return dp[i][C]
        x = 0
        if C- B[i] >= 0:
            x = A[i] + self.helper(A, B, C - B[i], i+1, n, dp, valSum)
        y = self.helper(A, B, C, i+1, n, dp, valSum)

        dp[i][C] = max(x, y)

        return dp[i][C]

#Complexity:
#Time: O(N*C)
#Space: O(N*C)
#where n is the size of the given arrays and C is the capacity

#Test Cases:
#[60, 100, 120], [10, 20, 30], 50
#[10, 20, 30, 40], [12, 13, 15, 19], 10

sol = Solution()

print(sol.solve([60, 100, 120], [10, 20, 30], 50))
print(sol.solve([10, 20, 30, 40], [12, 13, 15, 19], 10))

#Link: https://practice.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1