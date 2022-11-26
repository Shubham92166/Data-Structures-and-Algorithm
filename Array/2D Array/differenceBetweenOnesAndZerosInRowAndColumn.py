def onesMinusZeros(grid):
    n = len(grid)
    m = len(grid[0])
    
    rows = []
    cols = []
    
    for i in range(n):
        count = 0
        for j in range(m):
            if grid[i][j] == 1:
                count += 1
        rows.append(count)
    
    for i in range(m):
        count = 0
        for j in range(n):
            if grid[j][i] == 1:
                count += 1
        cols.append(count)
        
    matrix = [[0]*m for i in range(n)]
    
    
    for i in range(n):
        for j in range(m):
            matrix[i][j] = rows[i] + cols[j] - (n-rows[i]) - (m-cols[j])
    
    return matrix

#Complexity:
#Time: O(n*m)
#Space: O(n*m)
#Where n is the no. of rows and m is the no. of colums

#Test Cases:
#[[0,1,1],[1,0,1],[0,0,1]], [[1,1,1],[1,1,1]]

print(onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))
print(onesMinusZeros([[1,1,1],[1,1,1]]))

#Link: https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/