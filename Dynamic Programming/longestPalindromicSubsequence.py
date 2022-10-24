#Method-1: Using Top down approach + Dp
def longestPalindromeSubseq(s):
    n = len(s)
    dp = [[-1]*n for i in range(n)]
    
    return helper(s, s[::-1], 0, 0, n, dp)
    
def helper(a, b, i, j, n, dp):
    if i == n or j == n:
        return 0
    
    ans2 = 0
    ans3 = 0
    ans1 = 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    if a[i] == b[j]:
        ans1 = 1 + helper(a, b, i+1, j+1, n, dp)
    else:
        ans2 = helper(a, b, i, j+1, n, dp)
        ans3 = helper(a, b, i+1, j, n, dp)
    
    dp[i][j] = ans1 + max(ans2, ans3)
    return dp[i][j]

#Complexity:
#Time: O(n*n)
#Space O(n*n)

#Run:
print(longestPalindromeSubseq("bbbab"))
print(longestPalindromeSubseq("cbbd"))
print(longestPalindromeSubseq("abracadabra"))
print(longestPalindromeSubseq("af"))
print(longestPalindromeSubseq("a"))

#Method-2: USing Bottom-up approach + Dp

def longestPalindromeSubseq(s):
    n = len(s)
    dp = [[-1]*(n+1) for i in range(n+1)]
    
    for i in range(n+1):          
        for j in range(n+1):
            if i == n or j == n:
                dp[i][j] = 0
    return helper(s, s[::-1], n, dp)
    
def helper(s1, s2, n, dp):
    ans2 = 0
    ans3 = 0
    ans1 = 0
    
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i+1][j+1] 
                
            else:
                ans2 = dp[i][j+1]
                ans3 = dp[i+1][j]
                
                dp[i][j] = max(ans2, ans3)

    return dp[0][0]

#Complexity:
#Time: O(n*n)
#Space: O(n*n)

#Run:
print(longestPalindromeSubseq("bbbab"))
print(longestPalindromeSubseq("cbbd"))
print(longestPalindromeSubseq("abracadabra"))
print(longestPalindromeSubseq("af"))
print(longestPalindromeSubseq("a"))

#Test Cases:
"bbbab", #"cbbd", #"abracadabra", #"af", #"a"

#Link: https://leetcode.com/problems/longest-palindromic-subsequence/
