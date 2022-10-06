def lexicographicallySmallest (S, k):
    count = 0
    x = len(S)
    count = (x and (not(x & (x - 1))))
    
    if count == 1:
        k //= 2
    else:
        k *= 2
        
    if k >= x:
        return -1
        
    stack = []

    
    for index in range(len(S)):
        
        while stack and k > 0 and (stack[-1] > S[index]):
            stack.pop()
            k -= 1
    
        stack.append(S[index])
    
    
    while k and stack:
        stack.pop()
        k -= 1

    if k == 0 and stack:    
        return ''.join(stack)   
    return -1

#Complexity:
#Time: O(n+k)
#Space: O(n)

#Test Cases:
#"fooland", 2
#"code", 4
#"zwax", 1

print(lexicographicallySmallest("fooland", 2))
print(lexicographicallySmallest("code", 4))
print(lexicographicallySmallest("zwax", 1))

#Link: https://practice.geeksforgeeks.org/problems/mila-and-strings0435/1