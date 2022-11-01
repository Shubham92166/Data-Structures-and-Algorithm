from sys import maxsize
import math

def minFallingPathSum(matrix):
    r = len(matrix)
    dp = [[-1]*(r+1) for i in range(r+1)]
        
    minAns = math.inf
    for i in range(r):
        minAns = min(minAns, helper(matrix, 0, i, r, r, dp))
    return minAns

def helper(matrix, i, j, n, m, dp):
    if i >= n or j < 0 or j >= m:
        return float("inf")
    
    if i == n-1:
        return matrix[i][j]
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    ans1 = helper(matrix, i+1, j-1, n, m, dp)
    ans2 = helper(matrix, i+1, j, n, m, dp)
    ans3 = helper(matrix, i+1, j+1, n, m, dp)
    
    dp[i][j] =  matrix[i][j] + min(ans1, ans2, ans3)
    
    return dp[i][j]
    
#Complexity:
#Time: O(n^3)
#Space: O(n^2)

#Test Cases:
#[[2,1,3],[6,5,4],[7,8,9]], [[-19,57],[-40,-5]]

print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
print(minFallingPathSum([[-19,57],[-40,-5]]))

#Link: https://leetcode.com/problems/minimum-falling-path-sum/