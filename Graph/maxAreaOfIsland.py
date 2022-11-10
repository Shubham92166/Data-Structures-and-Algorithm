class Solution:
    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        visited = [[False]*n for i in range(m)]
        directions = [[0,-1], [0,1], [-1,0], [1,0]]

        maxCount = 0
        for i in range(m):
            for j in range(n):
                self.count = 0
                if grid[i][j] == 1 and not visited[i][j]:
                    maxCount = max(maxCount, self.dfs(grid, i, j, m, n, visited, directions))           
        return maxCount
        
    def dfs(self, grid, row, col, m, n, visited, directions):
        if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0 or visited[row][col]:
            return
        
        visited[row][col] = True
        self.count += 1

        for d in directions:
            self.dfs(grid, row + d[0], col + d[1], m, n, visited, directions)

        return self.count
    
#Complexity:
#Time: O(m*n)
#Space: O(m*n)
#Where m is the no. of rows and n is the no. of columns

#Test Cases:
#[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#[[0,0,0,0,0,0,0,0]]

sol = Solution()

print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(sol.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))

#Link: https://leetcode.com/problems/max-area-of-island/