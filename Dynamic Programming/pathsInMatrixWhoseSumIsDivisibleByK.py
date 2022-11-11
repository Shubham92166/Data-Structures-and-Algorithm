def numberOfPaths(grid, k):
    mRows = len(grid)
    nCols = len(grid[0])
    dp = [[[None]*k for j in range(nCols+1)] for i in range(mRows+1)]
    ans = minCost(grid, 0, 0, mRows, nCols, dp, k, 0)
    return ans % 1000000007

def minCost(input, row, col, mRows, nCols, dp, k, sumi):
    if row >= mRows or col >= nCols:
        return 0

    if row == mRows-1 and col == nCols-1:
        if (sumi + input[row][col]) % k == 0:
            return 1

    if dp[row][col][sumi] != None:
        return dp[row][col][sumi]


    ans1 = minCost(input, row, col+1, mRows, nCols, dp, k, (sumi + input[row][col]) % k) 
    ans2 = minCost(input, row+1, col, mRows, nCols, dp, k, (sumi + input[row][col]) % k)

    dp[row][col][sumi] = (ans1 + ans2) % 1000000007

    return dp[row][col][sumi] 

#Complexity:
#Time: O(m*n)
#Space: O(m*n)

#Test Cases:

#Link: https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/