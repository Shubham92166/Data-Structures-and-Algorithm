def longestPalindrome(A):
    maxLength = -1
    output = ''
    n = len(A)
    for i in range(n):
        l = i
        r = i
        while(l >= 0 and r < n and A[l] == A[r]):
            if r-l+1 > maxLength:
                maxLength = r-l+1
                output = A[l:r+1]
            l -= 1
            r += 1
    for i in range(n):
        l = i
        r = i+1
        while(l >= 0 and r < n and A[l] == A[r]):
            if r-l+1 > maxLength:
                maxLength = r-l+1
                output = A[l:r+1]
            l -= 1
            r += 1
    return output

#Test Cases:
#"babad", "cbbd"

#Complexity:
#Time: O(N2)
#Space: O(N)

print(longestPalindrome("cbbd"))
print(longestPalindrome("babad"))