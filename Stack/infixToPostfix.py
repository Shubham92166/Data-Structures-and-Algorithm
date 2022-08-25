def solve(A):
    stack = []
    res = ""
    A = "(" + A +")"
    for i in A:
        if i == "(":
            stack.append("(")
        elif i == "^":
            while stack and stack[-1] == "^":
                res += stack.pop()
            stack.append(i)
        elif i in "+-":
            while stack and stack[-1] in "+-*/^":
                res += stack.pop()
            stack.append(i)
        elif i in "/*":
            while stack and stack[-1] in "/*^":
                res += stack.pop()
            stack.append(i)
        elif i == ")":
            temp = ""
            while stack and stack[-1] != "(":
                temp += stack.pop()
            res += temp
            stack.pop()
        else:
            res += i
    return res

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"x^y/(a*z)+b", "a+b*(c^d-e)^(f+g*h)-i"

print(solve("x^y/(a*z)+b"))
print(solve("a+b*(c^d-e)^(f+g*h)-i"))

#Link: https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/