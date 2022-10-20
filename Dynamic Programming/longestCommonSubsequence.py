#Method-1: Using Top-down + Dp

def longestCommonSubsequence(text1, text2):
    n = len(text1)
    m = len(text2)
    dp = [[-1]*m for i in range(n)]
    
    return helper(text1, text2, 0, 0, n, m, dp)
    
def helper(a,b, i, j, n1, n2, dp):
    if i == n1 or j == n2:
        return 0
    
    ans2 = 0
    ans3 = 0
    ans1 = 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    if a[i] == b[j]:
        ans1 = 1+ helper(a, b, i+1, j+1, n1, n2, dp)
    else:
        ans2 = helper(a, b, i, j+1, n1, n2, dp)
        ans3 = helper(a, b, i+1, j, n1, n2, dp)
    
    dp[i][j] = ans1 + max(ans2, ans3)
    return dp[i][j] 

#Complexity:
#Time: O(n*m)
#Space: O(n*m)
#Where n is the length of text1 and m is the length of text2

#Run:
print(longestCommonSubsequence("abcde", "ace"))
print(longestCommonSubsequence("abc", "abc"))
print(longestCommonSubsequence("abc", "def"))

#Method-2: Using Bottom-up approach + Dp

def longestCommonSubsequence(text1, text2):
    n = len(text1)
    m = len(text2)
    dp = [[-1]*(m+1) for i in range(n+1)]
    
    for i in range(n+1):          
        for j in range(m+1):
            if i == n or j == m:
                dp[i][j] = 0
    return helper(text1, text2, n, m, dp)
    
    
def helper(a,b, n1, n2, dp):
    ans2 = 0
    ans3 = 0
    ans1 = 0
    
    for i in range(n1-1, -1, -1):
        for j in range(n2-1, -1, -1):
            if a[i] == b[j]:
                dp[i][j] = 1 + dp[i+1][j+1] 
                
            else:
                ans2 = dp[i][j+1]
                ans3 = dp[i+1][j]
                
                dp[i][j] = max(ans2, ans3)
    
    return dp[0][0]

#Complexity:
#Time: O(n*m)
#Space: O(n*m)
#Where n is the length of text1 and m is the length of text2

#Run:
print(longestCommonSubsequence("abcde", "ace"))
print(longestCommonSubsequence("abc", "abc"))
print(longestCommonSubsequence("abc", "def"))

#Test Cases:
#"abcde", "ace"
#"abc", "abc"
#"abc", "def"

#Link: https://leetcode.com/problems/longest-common-subsequence/


