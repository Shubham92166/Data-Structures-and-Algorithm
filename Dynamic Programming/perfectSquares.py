import math
def numSquares(n):
    dp = [-1]*(n+1)
    return countSquares(n, dp)
    
def countSquares(n, dp):
    if n <= 1:
        return n
    
    if dp[n] == -1:
        dp[n] = math.inf
    
        for i in range(1, int(math.sqrt(n))+1):
            dp[n] = min(dp[n], 1+countSquares(n-i*i, dp))
    
    return dp[n]

#Complexity:
#Time O(n)
#Space: O(n)

#Test Cases:
#12, 25, 13

print(numSquares(12))
print(numSquares(25))
print(numSquares(13))

#Link: https://leetcode.com/problems/perfect-squares/