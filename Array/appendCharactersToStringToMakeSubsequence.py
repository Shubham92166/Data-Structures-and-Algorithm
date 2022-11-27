def appendCharacters(s, t):
    k =0
    for i in range(len(s)):
        if k < len(t) and s[i] == t[k]:
            k += 1
        elif k == len(t):
            return 0
    return len(t) - k

#Complexity:
#Time: O(n1)
#Space: O(1)

#Test Cases:
#"coaching", "coding"
#"abcde", "a"
#"z", "abcde"

print(appendCharacters("coaching", "coding"))
print(appendCharacters("abcde", "a"))
print(appendCharacters("z", "abcde"))

#Link: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/