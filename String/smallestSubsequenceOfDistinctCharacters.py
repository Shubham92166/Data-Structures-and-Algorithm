def smallestSubsequence(s):
    stack = []
    dic = {}
    visited = set() 
    
    for i in range(len(s)):
        dic[s[i]] = i

    for i in range(len(s)):
        
        if s[i] not in visited:     
            while stack and stack[-1] > s[i] and dic[stack[-1]] > i:
                visited.remove(stack.pop())

            stack.append(s[i])
            visited.add(s[i])
        
    return "".join(stack)

#Complexity:
#Time: O(n)
#Space: O(n)

#Test cases:
#"bcabc", "cbacdcbc", "abracadabra"

print(smallestSubsequence("bcabc"))
print(smallestSubsequence("cbacdcbc"))
print(smallestSubsequence("abracadabra"))

#Link: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/