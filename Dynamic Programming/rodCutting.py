def cutRod(A, n):
    dp = [[0]*(n+1) for i in range(n+1)]
    return helper(A, 1, n, n, dp)

def helper(A, i, m, n, dp):
    for i in range(n-1, -1, -1):
        for j in range(n+1):
            cut = 0
            if i+1 <= j:
                cut = A[i] + dp[i][j-i-1]
            notCut = dp[i+1][j]
            dp[i][j] = max(cut, notCut)
    return dp[0][n]

#Complexity:
#Time: O(n*n)
#Space: O(n*n)

#Test Cases:
#[1, 5, 8, 9, 10, 17, 17, 20], 8
#[3, 5, 8, 9, 10, 17, 17, 20], 8

print(cutRod([1, 5, 8, 9, 10, 17, 17, 20], 8))
print(cutRod([3, 5, 8, 9, 10, 17, 17, 20], 8))

#Link: https://practice.geeksforgeeks.org/problems/rod-cutting0840/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article