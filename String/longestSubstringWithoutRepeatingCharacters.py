import math

def lengthOfLongestSubstring(s):
    lastSeen = {}
    l, r = 0, 0
    n = len(s)
    if n == 0:
        return 0
    maxLength = -math.inf
    while r < n:
        if lastSeen.get(s[r], -1) != -1:
            l = max(lastSeen.get(s[r])+1, l)
        lastSeen[s[r]] = r
        maxLength = max(maxLength, r-l+1)
        r += 1
    return maxLength

#Complexity:
#Time: O(n)
#Space: O(n)
#Where n is the length of the string

#Test Cases:
#"abcabcbb", "bbbbb", "pwwkew"

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))

#Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/