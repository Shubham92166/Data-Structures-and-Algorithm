def longestCommonSubstr(text1, text2, n, m):
    ans = 0
    
    dp = [[0]*(m+1) for i in range(n+1)]
    
    return helper(text1, text2, n, m, 0, 0, dp, ans)
    

def helper(a, b, n, m, i, j, dp, ans):
    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                
            else:
                dp[i][j] = 0
            ans = max(ans, dp[i][j])   
    return ans

#Complexity:
#Time: O(n*m)
#Space: O(n*m)

#Test Cases:
#"ABCDGH", "ACDGHR", 6, 6
#"ABC", "ACB", 3, 3

print(longestCommonSubstr("ABCDGH", "ACDGHR", 6, 6))
print(longestCommonSubstr("ABC", "ACB", 3, 3))

#Link: https://practice.geeksforgeeks.org/problems/longest-common-substring1452/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article