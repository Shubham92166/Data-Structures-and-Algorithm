def strStr( haystack, needle):    
    s = needle + "$" + haystack
    lps = [0]*len(s)
    for i in range(1, len(s)):
        x = lps[i-1]
        while s[x] != s[i]:
            if x == 0:
                x = -1
                break
            x = lps[x-1]
        lps[i] = x+1

    ans = 0
    for i in range(len(lps)):
        if lps[i] == len(needle):
            ans = i
            break
    
    if ans - len(needle)*2 >= 0:
        return ans - len(needle)*2
    return -1

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"hello", "ll"
#"aaaaa", "bba"
#"aaaa", "a"

print(strStr("hello", "ll"))
print(strStr("aaaaa", "bba"))
print(strStr("aaaa", "a"))

#Link: https://leetcode.com/problems/implement-strstr/