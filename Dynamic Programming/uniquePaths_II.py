from sys import maxsize
def uniquePathsWithObstacles(obstacleGrid):
    row = len(obstacleGrid)
    col = len(obstacleGrid[0])

    dp = [[maxsize for j in range(col+1)] for i in range(row+1)]

    return helper(obstacleGrid, 0, 0, row, col, dp)
     

def helper(A, i, j, row, col, dp):
    if i >= row or j >= col:
        return 0

    if A[i][j] == 1:
        return 0

    if i == row-1 and j == col-1:
        return 1

    if dp[i][j] != maxsize:
        return dp[i][j]
    ans1 = helper(A, i, j+1, row, col, dp)
    ans2 = helper(A, i+1, j, row, col, dp)
    dp[i][j] = ans1+ans2
    
    return ans1+ans2

#Complexity:
#Time: O(m*n)
#Space: O(m*n)
#where m is the no. of rows and n is the no. of columns

#Test Cases:
#[[0,0,0],[0,1,0],[0,0,0]], [[0,1],[0,0]]

print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(uniquePathsWithObstacles([[0,1],[0,0]]))

#Link: https://leetcode.com/problems/unique-paths-ii/