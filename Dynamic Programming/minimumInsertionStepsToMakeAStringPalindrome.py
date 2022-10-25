def minInsertions(s):
    n = len(s)
    dp = [[-1]*(n+1) for i in range(n+1)]
    
    return n-helper(s, s[::-1], 0, 0, n, dp)

def helper(s1, s2, i, j, n, dp):
    if i == n or j == n:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]
    
    if s1[i] == s2[j]:
        dp[i][j] = 1 + helper(s1, s2, i+1, j+1, n, dp)
    
    else:
        ans1 = helper(s1, s2, i, j+1, n, dp)
        ans2 = helper(s1, s2, i+1, j, n, dp)
        dp[i][j] = max(ans1, ans2)
    
    return dp[i][j]

#Complexity:
#Time: O(n^2)
#Space: O(n^2)
#Where n is the length of the given string

#Test Cases:
#"zzazz", "mbadm", "leetcode"

print(minInsertions("zzazz"))
print(minInsertions("mbadm"))
print(minInsertions("leetcode"))

#Link: https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/