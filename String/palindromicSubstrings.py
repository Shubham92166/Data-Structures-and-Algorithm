def countSubstrings(A):
    count = 0
    n = len(A)
    for i in range(n):
        l = i
        r = i
        while(l >= 0 and r < n and A[l] == A[r]):
            count += 1
            l -= 1
            r += 1
    for i in range(n):
        l = i
        r = i+1
        while(l >= 0 and r < n and A[l] == A[r]):
            count += 1
            l -= 1
            r += 1
    return count

#Test Cases:
#"abc", "aaa"

#Complexity:
#Time Complexity: O(N2)
#Space: O(1)

print(countSubstrings("aaa"))
print(countSubstrings("abc"))