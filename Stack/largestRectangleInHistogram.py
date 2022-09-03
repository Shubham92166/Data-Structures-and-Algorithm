import math
def largestRectangleArea(A):
    length = len(A)
    if len(A) == 1:
        return A[0]
    left = []
    stack = []
    for i in range(len(A)):
        while stack and A[stack[-1]] >= A[i]:
            stack.pop()
        if stack:
            left.append(stack[-1]+1)
        else:
            left.append(0)
        stack.append(i)
    
    right = []
    stack = []
    
    for i in range(len(A)-1, -1, -1):
        while stack and A[stack[-1]] >= A[i]:
            stack.pop()
        if stack:
            right.append(stack[-1]-1)
        else:
            right.append(length-1)
        stack.append(i)
    right = right[::-1]
    
    maxArea = -math.inf
    for i in range(len(A)):
        
        width = right[i]-left[i]+1
        height = A[i]
        maxArea = max(maxArea, width*height)
    
    return maxArea

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[2,1,5,6,2,3], [2,4]

print(largestRectangleArea([2,1,5,6,2,3]))
print(largestRectangleArea([2,4]))

#Link: https://leetcode.com/problems/largest-rectangle-in-histogram/