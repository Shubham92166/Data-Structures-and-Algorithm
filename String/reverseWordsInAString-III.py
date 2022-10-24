def reverseWords(s):
    s = s.split()
    return " ".join(i[::-1] for i in s)

#Complexity:
#Time: O(nm)
#Space: O(n)
#where n is the no. of words and m is the length of longest word

#Test Cases:
#"Let's take LeetCode contest", "God Ding"

print(reverseWords("Let's take LeetCode contest"))
print(reverseWords("God Ding"))

#Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/