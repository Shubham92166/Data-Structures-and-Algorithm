def solve(A, B):
    s = B + '$' + A 
    lps = [0]* len(s)
    for i in range(1, len(s)):
        x = lps[i-1]
        while s[x] != s[i]:
            if x == 0:
                x = -1
                break
            x = lps[x-1]
        lps[i] = x+1
    k = len(B)
    count = 0
    for i in lps:
        if i == k:
            count += 1
    return count

#Complexity:
#Time: O(n+m)
#Space: O(n+m)
#n is the length of A and m is the length of B

#Test Cases:
#"abababa", "aba" 
#"mississipi", "ss"
#"hello", "hi"

print(solve("abababa", "aba"))
print(solve("mississipi", "ss"))
print(solve("hello", "hi"))  