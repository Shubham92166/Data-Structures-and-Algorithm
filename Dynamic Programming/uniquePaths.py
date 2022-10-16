from sys import maxsize

#Method-1: Using Top down approach

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

#Run:
print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
print(uniquePaths(51, 9))

#Method-2: Bottom up approach

def uniquePaths(m, n):
    dp = [[0 for j in range(n+1)] for i in range(m+1)]
    dp[-1][-2] = 1
    return helper(m, n, dp)

def helper(row, col, dp):
    for i in range(row-1, -1, -1):
        for j in range(col-1, -1, -1):
            dp[i][j] = dp[i][j+1] + dp[i+1][j]
    
    return dp[0][0]

#complexity:
#Time: O(m*n)
#Space: O(m*n)

#Run:
print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
print(uniquePaths(51, 9))

#Method-3: Using Bottom up approach + space optimization

def uniquePaths(m, n):
    dp = [0 for i in range(n+1)]
    dp[-2] = 1
    return helper(m, n, dp)
    
def helper(row, col, prev):
    for i in range(row-1, -1, -1):
        cur = [0]* (col+1)
        for j in range(col-1, -1, -1):
            cur[j] = cur[j+1] + prev[j]
        prev = cur
    
    return cur[0]

#complexity:
#Time: O(m*n)
#Space: O(n)

#Run:
print(uniquePaths(3, 7))
print(uniquePaths(3, 2))
print(uniquePaths(51, 9))

#Test Cases:
#3, 7
#3, 2
#51, 9

#Link: https://leetcode.com/problems/unique-paths/