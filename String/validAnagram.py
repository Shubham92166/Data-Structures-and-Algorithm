#Approach: We create two dictionaries for s and t string. We then compare it character by character. If both the dictionaries have all
#characters same number number of times then we return True else False. However, in the beginning we check, if the length of both the 
#strings are same or not. Because the prerequisite for anagram is all the characters should be present in both the strings and same 
#number of times. This means that the length should be same for both the strings. If not, then we can directly return False.
#We are using hashmap here so that the frequency of each character can be accessed in O(1) time.

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
#Time: O(n+m)
#Space: O(1)
#n is the length of s and m is the length of m

#Note: Since there are only 26 lower case characters so the space complexity is O(26) i.e., O(1)

#Test Cases:
#"anagram", "nagaram"
#"rat", "car"

print(isAnagram("rat", "car"))
print(isAnagram("anagram", "nagaram"))

#Link: https://leetcode.com/problems/valid-anagram/