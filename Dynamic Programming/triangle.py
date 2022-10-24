def minimumTotal(triangle):
    rows = len(triangle)
    dp = triangle.copy()
    helper(triangle, rows-1, dp)
    return dp[0][0]

def helper(triangle, rows, dp):
    for row in range(rows-1, -1, -1):
        for col in range(row+1):  
            dp[row][col] += min(dp[row+1][col], dp[row+1][col+1])

#complexity:
#Time: O(n)
#Space: O(n*m)
#where n is the no. of rows and m is the no. of columns

#Test cases:
#[[2],[3,4],[6,5,7],[4,1,8,3]], [[-10]]

print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(minimumTotal([[-10]]))

#Link: https://leetcode.com/problems/triangle/
