#Method-1: Using Top down approach + Dp

def minDistance(word1, word2):
    n = len(word1)
    m = len(word2)
    dp = [[-1]*(m+1) for i in range(n+1)]
    
    return helper(word1, word2, 0, 0, n, m, dp)

def helper(s1, s2, i, j, n, m, dp):
    if i == n:
        return m-j

    if j == m:
        return n-i

    ans1 = 0
    ans2 = 0
    ans3 = 0

    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i] == s2[j]:
        dp[i][j] = helper(s1, s2, i+1, j+1, n, m, dp)
        return dp[i][j]
      
    else:
        ans1 = helper(s1, s2, i+1, j+1, n, m, dp)
        ans2 = helper(s1, s2, i, j+1, n, m, dp)
        ans3 = helper(s1, s2, i+1, j, n, m, dp)
        
        dp[i][j] = 1 + min(ans1, ans2, ans3)
        return dp[i][j]

#Complexity:
#Time: O(n*m)
#Space: O(n*m)

#Run:
print(minDistance("horse", "ros"))
print(minDistance("intention", "execution"))

#Method-2: Using Bottom up approach + Dp

def minDistance(word1, word2):
    n = len(word1)
    m = len(word2)
    dp = [[-1]*(m+1) for i in range(n+1)]
    
    return helper(word1, word2, n, m, dp)

def helper(s1, s2, n, m, dp):
    for i in range(n, -1, -1):
        for j in range(m, -1, -1):
            if i == n:
                dp[i][j] = m-j
                continue
            
            if j == m:
                dp[i][j] = n-i
                continue
            
            ans1 = 0
            ans2 = 0
            ans3 = 0
            
            if s1[i] == s2[j]:
                dp[i][j] = dp[i+1][j+1]
                continue

            else:
                ans1 =  dp[i+1][j+1]
                ans2 = dp[i][j+1]
                ans3 = dp[i+1][j]

                dp[i][j] = 1 + min(ans1, ans2, ans3)
    return dp[0][0]

#Complexity:
#Time: O(n*m)
#Space: O(n*m)

#Run:
print(minDistance("horse", "ros"))
print(minDistance("intention", "execution"))

#Test Cases:
#"horse", "ros"
#"intention", "execution"

#Link: https://leetcode.com/problems/edit-distance/