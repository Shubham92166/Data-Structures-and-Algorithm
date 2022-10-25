def isInterleave(s1, s2, s3):
    dic = {}
    n = len(s1)
    m = len(s2)
    l = len(s3)
    if n+m != l:
        return False

    return helper(0, 0, 0, s1, s2, s3, n, m, l, dic)

def helper(i, j, k, s1, s2, s3, n, m, l, dic):
    if k == l:
        return True
    
    if dic.get((i, j, k), -1) != -1:
        return dic.get((i, j, k))
    
    ans1 = False
    ans2 = False
    
    if i < n and k < l and s1[i] == s3[k]:
        ans1 = helper(i+1, j, k+1, s1, s2, s3, n, m, l, dic)
        dic[(i, j, k)] = ans1
    
    if j < m and k < l and s2[j] == s3[k]:
        ans2 = helper(i, j+1, k+1, s1, s2, s3, n, m, l, dic)
        dic[(i, j, k)] = ans2
    
    return ans1 or ans2

#Complexity:
#Time: O(n*m)
#Space: O(n*m)

#Test Cases:
#"aabcc", "dbbca", "aadbbcbcac"
#"aabcc", "dbbca", "aadbbbaccc"
#"", "", ""

print(isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(isInterleave("aabcc", "dbbca", "aadbbbaccc"))
print(isInterleave("", "", ""))

#Link: https://leetcode.com/problems/interleaving-string/