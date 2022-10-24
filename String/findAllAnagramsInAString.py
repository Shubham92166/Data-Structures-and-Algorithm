def findAnagrams(s, p):
    dic1 = {}
    dic2 = {}
    
    if len(p) > len(s):
        return []
    
    ans = []
    for i in p:
        dic1[i] = dic1.get(i, 0) + 1
    
    pos = 0
    
    for i in range(0, len(p)):
        dic2[s[i]] = dic2.get(s[i], 0) + 1
    
    if compareDict(dic1, dic2) == True:
        ans.append(0)
    
    for i in range(len(p), len(s)):
        dic2[s[pos]] -= 1

        if dic2.get(s[pos], 0) == 0:
            del dic2[s[pos]]
            
        pos += 1
        dic2[s[i]] = dic2.get(s[i], 0) + 1  
        
        if compareDict(dic1, dic2) == True:
            ans.append(i-len(p)+1)
    
    return ans

def compareDict(dic1, dic2):
    if len(dic1) != len(dic2):
        return False
    
    for key, val in dic1.items():
        if dic2.get(key) != val:
            return False
    return True

#Complexity:
#Time: O(n)
#Space: O(1)
#n is the length of s

#Test Cases:
#"cbaebabacd", "abc"
#"abab", "ab"

print(findAnagrams("cbaebabacd", "abc"))
print(findAnagrams("abab", "ab"))

#Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/