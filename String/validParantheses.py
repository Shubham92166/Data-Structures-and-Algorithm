from turtle import isvisible


def isValid(s):
    stack = []
    if(len(s) == 1):
        return False
    for bracket in s:
        if(bracket in ["(", "{", "["]):
            stack.append(bracket)
        else:
            if(not stack):
                return False
            current_char = stack.pop()
            if(current_char == "(" and bracket != ")"):
                return False
            elif(current_char == "{" and bracket != "}"):
                return False
            elif(current_char == "[" and bracket != ']'):
                return False
    if(not stack):
        return True
    else:
        return False

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"()", "()[]{}", "(]", "){", "{[]}", "]", "([)]"

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("){"))
print(isValid("{[]}"))
print(isValid("]"))
print(isValid("([)]"))

#Link: https://leetcode.com/problems/valid-parentheses/