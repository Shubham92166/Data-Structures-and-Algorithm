def maxSum(grid):
    n = len(grid)
    m = len(grid[0])
    maxSum = 0
    sum = 0
    for i in range(n-3+1):
        for j in range(m-3+1):
            p = i
            q = j
            sum = 0
            sum += grid[p][q]
            sum += grid[p][q+1]
            sum += grid[p][q+2]
            sum += grid[p+1][q+1]
            sum += grid[p+2][q]
            sum += grid[p+2][q+1]
            sum += grid[p+2][q+2]
            
            maxSum = max(maxSum, sum)
    
    return maxSum

#Complexity:
#Time: O(n*m)
#Space: O(1)
#where n is the no. of rows and m is the no. of columns

#Test Cases:
#[[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]], [[1,2,3],[4,5,6],[7,8,9]]

print(maxSum([[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]))
print(maxSum([[1,2,3],[4,5,6],[7,8,9]]))

#Link: https://leetcode.com/problems/maximum-sum-of-an-hourglass/