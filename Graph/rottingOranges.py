import queue, math

def orangesRotting(grid):
    m = len(grid)
    n = len(grid[0])
    
    flag = False

    
    matrix = [[math.inf]*(n) for i in range(m)]
    
    q = queue.Queue()
    
    empty, fresh, rotten = 0, 1, 2
    for row in range(m):
        for col in range(n):
            if grid[row][col] == rotten:
                q.put((row, col, 0))
                flag = True
    
    while not q.empty():
        row, col, days = q.get()
        
        if matrix[row][col] != math.inf:
            continue
        
        matrix[row][col] = days
        
        if row + 1 < m and grid[row+1][col] == fresh:
            q.put((row+1, col, days+1))
        
        if row-1 >= 0 and grid[row-1][col] == fresh:
            q.put((row-1, col, days+1))
        
        if col+1 < n and grid[row][col+1] == fresh:
            q.put((row, col+1, days+1))
            
        if col-1 >= 0 and grid[row][col-1] == fresh:
            q.put((row, col-1, days+1))
    
    ans = -math.inf
    
    for row in range(m):
        for col in range(n):
            if grid[row][col] != empty:
                ans = max(ans, matrix[row][col])
                flag = True
                
    if flag:
        if ans == math.inf:
            return -1
        else:
            return ans
    else:
        return 0

#Complexity:
#Time: O(m*n)
#Space: O(m*n)
#Where m is the no. of rows and n is the no. of columns of the grid

#Test Cases:
#[[2,1,1],[0,1,1],[1,0,1]], [[0,2]]

print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(orangesRotting([[0,2]]))

#Link: https://leetcode.com/problems/rotting-oranges/