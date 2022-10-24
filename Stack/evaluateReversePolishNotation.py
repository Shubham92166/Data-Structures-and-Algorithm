def evalRPN(tokens):
    stack = []
    for i in tokens:
        if i not in "+-*/":
            stack.append(int(i))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if i == "+":
                stack.append(op1+op2)
            elif i == "-":
                stack.append(op2-op1)
            elif i == "*":
                stack.append(op1*op2)
            elif i == "/":
                stack.append(int(op2/op1))
    return stack.pop()

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#["2","1","+","3","*"], ["4","13","5","/","+"], ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(evalRPN(["2","1","+","3","*"],))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

#Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/