def isValid(s):
    stack=[]
    for bracket in s:
        if(bracket in ["(", "{","["]):
            stack.append(bracket)
        else:
            if(not stack):
                return False
            current_char=stack.pop()
            if(current_char=="(" and bracket!=")"):
                return False
            elif(current_char=="{" and bracket!="}"):
                return False
            elif(current_char=="[" and bracket!=']'):
                return False
    if(len(stack)==0):
        return True
    else:
        return False

#Test Case: "){", "]", "{[]}", "([)]"

#Complexity:
#Time: O(n)
#Space: O(n) #for stack

print(isValid("]"))
print(isValid("{[]}"))
print(isValid("([)]"))