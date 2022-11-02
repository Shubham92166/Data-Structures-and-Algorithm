def shortestCommonSupersequence(str1, str2):
    n = len(str1)
    m = len(str2)
    ans = 0
    dp = [[0]*(m+1) for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):

            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                ans2 = dp[i][j-1]
                ans3 = dp[i-1][j]
                dp[i][j] = max(ans2, ans3)
            
    final = ""
    
    i, j = n, m
    
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            final += str1[i-1]
            i -= 1
            j -= 1

        elif dp[i][j-1] > dp[i-1][j]:
            final += str2[j-1]
            j -= 1

        else:
            final += str1[i-1]
            i -= 1
    
    while i > 0:
        final += str1[i-1]
        i -= 1
    
    while j > 0:
        final += str2[j-1]
        j -= 1
    
    return final[::-1]

#Complexity:
#Time: O(n*m)
#Space: O(n*m)
#Where n is the length of str1 and m is the length of str2

#Test Cases:
#"abac", "cab", 
#"aaaaaaaa", "aaaaaaaa"

print(shortestCommonSupersequence("abac", "cab"))
print(shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa"))

#Link: https://leetcode.com/problems/shortest-common-supersequence/