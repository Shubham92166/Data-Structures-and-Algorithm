from sys import setrecursionlimit
setrecursionlimit(10**8)

def solve(A, B, C):
    dp = [[-1 for i in range(B+1)] for i in range(A+1)]
    return helper(A, B, C, dp) % C
    
def helper(n, r, m, dp):
    if r == 1:
        return n
    
    if r == n or r == 0:
        return 1
    
    if dp[n][r] != -1:
        return dp[n][r]
    
    ans1 = helper(n-1, r, m, dp) % m
    ans2 = helper(n-1, r-1, m, dp) % m

    dp[n][r] = (ans1 + ans2) % m
    return dp[n][r]

#Complexity:
#Time: O(A*B)
#Space: O(A*B)

#Test Cases:
#5, 2, 13
#6, 2, 13

print(solve(5,2,13))
print(solve(6, 2, 13))

#Link: https://practice.geeksforgeeks.org/problems/ncr1019/1?page=1&category[]=Dynamic%20Programming&sortBy=submissions