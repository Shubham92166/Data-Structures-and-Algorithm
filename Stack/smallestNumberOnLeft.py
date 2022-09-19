def leftSmaller(a):
    ans = []
    stack = []
    
    for num in a:
        while stack and stack[-1] >= num:
            stack.pop()
            
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
        
        stack.append(num)
    return ans

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1, 6, 2], [1, 5, 0, 3, 4, 5]

print(leftSmaller([1, 6, 2]))
print(leftSmaller([1, 5, 0, 3, 4, 5]))

#Link: https://practice.geeksforgeeks.org/problems/smallest-number-on-left3403/1