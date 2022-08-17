def longestPrefix(s):
    lps = [0]* len(s)
    for i in range(1, len(s)):
        x = lps[i-1]
        while s[x] != s[i]:
            if x == 0:
                x = -1
                break
            x = lps[x-1]
        lps[i] = x+1
    
    val = lps[-1]
    return s[:val]

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"level", "ababab", "bba"

print(longestPrefix("level"))
print(longestPrefix("ababab"))
print(longestPrefix("bba"))