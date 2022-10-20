#Approach:
#This problem can be views as Largest Rectangle in a Histogram. Here for each row, we need to apply the same logic as Largest Rectangle
#in a Histogram and find the maximum area out of all rows.

#Method-1: Space is not optimized

import math
def maximalRectangle(A):
    n = len(A)
    m = len(A[0])
    d = A.copy()
    for i in range(n):
        for j in range(m):
            d[i][j] = int(d[i][j])
            
    for i in range(1, n):
        for j in range(m):
            if d[i][j] == 1:
                d[i][j] += int(d[i-1][j])
                
    area = []
    for row in range(n):
        area.append(findArea(A[row]))
    
    return max(area)

def findArea(A):
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
        maxArea = max(maxArea, (width*height))
    
    return maxArea

#Complexity:
#Time: O(n*m)
#Space: O(n*m)
#Where n is the no. of rows and m is the no. of columns

#Run:
print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(maximalRectangle([["0"]]))
print(maximalRectangle([["1"]]))
print(maximalRectangle([["1","1"]]))
print(maximalRectangle([["1","1"]]))

#Method-2: Space is Optimized:

def maximalRectangle(A):
    n = len(A)
    m = len(A[0])
    
    prev = [0]*m
    
    area = []
    
    for i in range(n):
        cur = A[i].copy()
        for j in range(m):
            cur[j] = int(cur[j])
            
            if cur[j] == 1:
                cur[j] += prev[j]

        area.append(findArea(cur))
        prev = cur
    
    return max(area)

def findArea(A):
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
        maxArea = max(maxArea, (width*height))
    
    return maxArea

#Complexity:
#Time: O(n*m)
#Space: O(m)
#Where n is the no. of rows and m is the no. of columns

#Run:
print(maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
print(maximalRectangle([["0"]]))
print(maximalRectangle([["1"]]))
print(maximalRectangle([["1","1"]]))
print(maximalRectangle([["1","1"]]))

#Test Cases:
#[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#[["0"]]
#[["1"]]
#[["1","1"]]
#[["0","0"]]

#Link: https://leetcode.com/problems/maximal-rectangle/