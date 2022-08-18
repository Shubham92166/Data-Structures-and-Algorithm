def maxPower(s):
    current_char = s[0]
    count = 0
    max = 0
    for char in s:
        if(current_char != char):
            current_char = char
            count = 1
        else:
            count += 1
        if(max < count):
            max = count
    return max

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#"leetcode", "abbcccddddeeeeedcba"

print(maxPower("leetcode"))
print(maxPower("abbcccddddeeeeedcba"))

#Link: https://leetcode.com/problems/consecutive-characters/