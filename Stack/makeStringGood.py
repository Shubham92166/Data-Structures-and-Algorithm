def makeGood(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else: 
            if s[i].islower() and stack[-1].isupper() and s[i] == stack[-1].lower():
                    stack.pop()
            elif s[i].isupper() and stack[-1].islower() and s[i] == stack[-1].upper():
                    stack.pop()
            else:
                stack.append(s[i])
    return "".join(stack)

#Test Case: "leEeetcode", "abBAcC", "s"

#Complexity:
#Time: O(N)
#Space: O(N) #for stack

print(makeGood("s"))
print(makeGood("abBAcC"))
print(makeGood("leEeetcode"))


