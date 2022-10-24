def braces(A):
    stack = []
    for i in A:
        if i in "+-*/(":
            stack.append(i)
        elif i == ")":
            if not stack:
                return 1
            else:
                if stack[-1] not in "+-*/":
                    return 1
                while stack and stack[-1] in "+-*/":
                    stack.pop()
                if stack[-1] != "(":
                    return 1
                stack.pop()
    return 0

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"((a+b))", "(a+(a+b))"

print(braces("((a+b))"))
print(braces("(a+(a+b))"))

#Link: https://www.geeksforgeeks.org/expression-contains-redundant-bracket-not/