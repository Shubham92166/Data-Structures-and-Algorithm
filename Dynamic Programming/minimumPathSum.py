from sys import maxsize
def minPathSum(grid):
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [[maxsize for j in range(cols+1)] for i in range(rows+1)]
        
        return minPath(grid, 0, 0, rows, cols, dp)
    
def minPath(grid, i, j, n, m, dp):
    if i == n-1 and j == m-1:
        return grid[i][j]
    if i >= n or j >= m:
        return maxsize
    
    if dp[i+1][j] == maxsize:
        ans1 = minPath(grid, i+1, j, n, m, dp)
        dp[i+1][j] = ans1
    else:
        ans1 = dp[i+1][j]
    
    if dp[i][j+1] == maxsize:
        ans2 = minPath(grid, i, j+1, n, m, dp)
        dp[i][j+1] = ans2
    else:
        ans2 = dp[i][j+1] 
    
    ans = grid[i][j]+min(ans1, ans2)
    return ans

#Test Cases:
#[[1,3,1],[1,5,1],[4,2,1]], [[1,2,3],[4,5,6]]

#Complexity:
#Time:
#Space:

print(minPathSum([[1,2,3],[4,5,6]]))
print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))


    