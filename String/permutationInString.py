def checkInclusion(A, B):
    if len(B) < len(A):
        return False

    dic1 = {}
    dic2 = {}
    count = 0
    n = len(A)

    for i in A:
        dic1[i] = dic1.get(i, 0)+1

    for i in range(len(A)):
        dic2[B[i]] = dic2.get(B[i], 0)+1
    found = check(dic1, dic2)
    if found:
        return found

    k = 0
    for j in range(n, len(B)):
        dic2[B[j]] = dic2.get(B[j], 0) + 1
        dic2[B[k]] = dic2.get(B[k], 0) - 1
        if dic2[B[k]] == 0:
            del dic2[B[k]]
        k += 1
        found = check(dic1, dic2)
        if found:
            return True
        
    return False

def check(dic1, dic2):
    count = 0
    for i in dic1:
        freq = dic1.get(i)
        if dic2.get(i) != freq :
            return False
    return True

#Complexity:
#Time: O(m)
#Space: O(m)
#m is the length of B

#Test Cases:
#"ab", "eidbaooo"
#"ab", "eidboaoo"
#"ab", "a"

#Link: https://leetcode.com/problems/permutation-in-string/