import math

def longestIncreasingPath(matrix):
    m = len(matrix)
    n = len(matrix[0])
    ans = -math.inf
    
    dp = [[None]*(n+1) for i in range(m+1)]
    for i in range(m):
        for j in range(n):
            ans = max(ans, helper(matrix, i, j, -1, m, n, dp))
    return ans

def helper(matrix, i, j, prev, m, n, dp):
    if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= prev:
        return 0
    
    if dp[i][j] != None:
        return dp[i][j]
    
    up = helper(matrix, i-1, j, matrix[i][j], m, n, dp)
    down = helper(matrix, i+1, j, matrix[i][j], m, n, dp)
    left = helper(matrix, i, j-1, matrix[i][j], m, n, dp)
    right = helper(matrix, i, j+1, matrix[i][j], m, n, dp)
    
    dp[i][j] = 1 + max(left, right, up, down)
    
    return dp[i][j]

#Complexity:
#Time: 
#Space: O(n*m)
#where n is the no. of rows and m is the no. of columns

#Test Cases:
#[[9,9,4],[6,6,8],[2,1,1]]
#[[3,4,5],[3,2,6],[2,2,1]]
#[[1]]
#[[1,2]]
#[[74,26,74]]
#[[45,12,63],[852,123,94]] 

print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))
print(longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))
print(longestIncreasingPath([[1]]))
print(longestIncreasingPath([[1,2]]))
print(longestIncreasingPath([[74,26,74]]))
print(longestIncreasingPath([[45,12,63],[852,123,94]]))

#Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/