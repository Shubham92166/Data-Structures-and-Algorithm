def numIslands(grid):
    m = len(grid)
    n = len(grid[0])
    
    visited = [[False]*n for i in range(m)]
    directions = [[0,-1], [0,1], [-1,0], [1,0]]

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and not visited[i][j]:
                dfs(grid, i, j, m, n, visited, directions)
                count += 1
    return count
        
def dfs(grid, row, col, m, n, visited, directions):
    if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == "0" or visited[row][col]:
        return
    
    visited[row][col] = True
    
    for d in directions:
        dfs(grid, row + d[0], col + d[1], m, n, visited, directions)

#Complexity:
#Time: O(m*n)
#Space: O(m*n)

#Test Cases:
#[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
#[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
#[["0", "0", "1", "0", "1", "0", "1", "1", "1"], ["0", "1", "0", "0", "1", "1", "1", "0", "1"]]
#[["1","1","1"],["0","1","0"],["1","1","1"]]

print(numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))
print(numIslands([["0", "0", "1", "0", "1", "0", "1", "1", "1"], ["0", "1", "0", "0", "1", "1", "1", "0", "1"]]))
print(numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))

#Link: https://leetcode.com/problems/number-of-islands/