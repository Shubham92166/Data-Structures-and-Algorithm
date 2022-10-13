from sys import maxsize
def uniquePaths(m, n):
    dp = [[maxsize for j in range(n+1)] for i in range(m+1)]

    ans = helper(0, 0, m, n, dp)
    return ans

def helper(i, j, row, col, dp):
    
    if i >= row or j >= col:
        return 0

    if i == row-1 and j == col-1:
        return 1

    if dp[i][j] != maxsize:
        return dp[i][j]

    ans1 = helper(i, j+1, row, col, dp)
    ans2 = helper(i+1, j, row, col, dp)
    dp[i][j] = ans1+ans2
    
    return dp[i][j]

#complexity:
#Time: O(m*n)
#Space: O(m*n)

#Test Cases:
#3, 7
#3, 2
#51, 9

print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
print(uniquePaths(51, 9))

#Link: https://leetcode.com/problems/unique-paths/