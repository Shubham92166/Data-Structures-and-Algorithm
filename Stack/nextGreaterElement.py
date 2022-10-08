from textwrap import indent
from tkinter import N


def nextGreater(arr):
    stack = []
    n = len(arr)    
    ans = [-1]*n 
    index = n-1
    for i in range(len(arr)-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        if stack:
            ans[index] = stack[-1]
        
        index -= 1

        stack.append(arr[i])
    return ans

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1, 3, 2, 4], [6, 8, 0, 1, 3]

print(nextGreater([1, 3, 2, 4]))
print(nextGreater([6, 8, 0, 1, 3]))

#Link: https://www.geeksforgeeks.org/next-greater-element/