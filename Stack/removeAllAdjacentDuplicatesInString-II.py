def removeDuplicates(s, k):
    stack = []
    for char in s:
        if stack and char == stack[-1][0]:
            count = stack[-1][1]+1
            stack.append([char, count])
            if count == k:
                delete(stack, k)
        else:
            stack.append([char, 1])
            
    ans = ""
    for i in stack:
        ans += i[0]
    return ans

def delete(stack, k):
    for i in range(k):
        stack.pop()

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"abcd", 2
#"deeedbbcccbdaa", 3
#"pbbcggttciiippooaais", 2

print(removeDuplicates("abcd", 2))
print(removeDuplicates("deeedbbcccbdaa", 3))
print(removeDuplicates("pbbcggttciiippooaais", 2))

#Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/