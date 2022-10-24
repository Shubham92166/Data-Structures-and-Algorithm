def removeStars(s):
    stack = []
    for i in s:
        if i == "*":
            if stack:
                stack.pop()
            else:
                break
        else:
            stack.append(i)
    return "".join(stack)

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"leet**cod*e", "erase*****"

print(removeStars("leet**cod*e"))
print(removeStars("erase*****"))

#Link: https://leetcode.com/problems/removing-stars-from-a-string/