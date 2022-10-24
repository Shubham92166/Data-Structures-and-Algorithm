def minLength(s, n): 
    stack = []
    pairs = ["12", "21", "34", "43", "56", "65", "78", "87", "09", "90"]
    for i in range(n):
        
        stack.append(s[i])
        
        while len(stack) >= 2 and str(stack[-1]) + str(stack[-2]) in pairs:
            stack.pop()
            stack.pop()
    
    return len(stack)

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"12213", 5
#"1350", 4

print(minLength("12213", 5))
print(minLength("1350", 4))

#Link: https://practice.geeksforgeeks.org/problems/904237fa926d79126d42c437802b04287ea9d1c8/1