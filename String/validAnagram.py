def isAnagram(s, t):
    if len(s) != len(t):
        return False
    dic1 = {}
    dic2 = {}
    for i in s:
        dic1[i] = dic1.get(i, 0) + 1
        
    for i in t:
        dic2[i] = dic2.get(i, 0) + 1
    
    for key, val in dic1.items():
        if dic2.get(key, -1) != val:
            return False
    return True

#Complexity:
#Time: O(1)
#Space: O(1)

#Note: Since there are only 26 lower case characters so the time and space complexity is O(26)

#Test Cases:
#"anagram", "nagaram"
#"rat", "car"

print(isAnagram("rat", "car"))
print(isAnagram("anagram", "nagaram"))

#Link: https://leetcode.com/problems/valid-anagram/