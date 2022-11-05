import math

def solve(A):
    n = len(A)-1
    dp = [[math.inf]*(n) for i in range(n)]
    return helper(A, 0, n-1, dp)
    
def helper(A, s, e, dp):
    if e == s:
        return 0

    ans = math.inf

    if dp[s][e] != math.inf:
        return dp[s][e]

    for m in range(s, e):
        val = (A[s] * A[m+1] * A[e+1]) + helper(A, s, m, dp) + helper(A, m+1, e, dp)
        dp[s][e] = min(dp[s][e], val)

    return dp[s][e]

#Complexity:
#Time: O(n^2)
#Space: O(n^2)
#Where n is the size of the array

#Test Cases:
#[40, 20, 30, 10, 30], [10, 20, 30]

print(solve([40, 20, 30, 10, 30]))
print(solve([10, 20, 30]))

#Link: https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article