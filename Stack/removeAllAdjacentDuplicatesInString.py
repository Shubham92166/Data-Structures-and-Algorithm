def removeDuplicates(s):
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        else:
            if char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
    return "".join(stack)


#Test Case: "abbaca", "azxxzy"

#Complexity:
#Time: O(N)
#Space: O(N)

print(removeDuplicates("azxxzy"))
print(removeDuplicates("abbaca"))
