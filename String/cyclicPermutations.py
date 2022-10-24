def solve(A, B):
    t = B+B
    s = A + "$" + t
    lps = [0]*len(s)
    for i in range(1, len(s)):
        x = lps[i-1]
        while s[x] != s[i]:
            if x == 0:
                x = -1
                break
            x = lps[x-1]
        lps[i] = x+1
    
    count = 0

    for i in lps:
        if i == len(A):
            count += 1
    if A == B:
        count -= 1 
    return count

#Complexity:
#Time: O(n+m)
#Space: O(n+m)
#n is the length of A and m is the length of B

#Test Cases:
#"1001", "0011"
#"111", "111"

print(solve("1001", "0011"))
print(solve("111", "111"))

#Link: https://www.geeksforgeeks.org/count-of-cyclic-permutations-having-xor-with-other-binary-string-as-0/