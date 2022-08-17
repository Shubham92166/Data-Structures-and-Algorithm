def shortestPalindrome(s):
    st = s
    n = len(st)
    rev = s[::-1]
    s = st + "$" + rev
    lps = [0]*len(s)
    
    for i in range(1, len(s)):
        x = lps[i-1]
        while s[x] != s[i]:
            if x == 0:
                x = -1
                break
            x = lps[x-1]
        lps[i] = x+1
        
    count = n-lps[2*n]
    return rev[:count] + st

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"aacecaaa", "abcd"

print(shortestPalindrome("aacecaaa"))
print(shortestPalindrome("abcd"))
