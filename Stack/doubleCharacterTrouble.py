def solve(A):
    stack = []
    for i in A:
        if not stack:
            stack.append(i)
        else:
            if i != stack[-1]:
                stack.append(i)
            else:
                while stack and stack[-1] == i:
                    stack.pop()
    return "".join(stack)

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"abccbc", "ab"

print(solve("abccbc"))
print(solve("ab"))