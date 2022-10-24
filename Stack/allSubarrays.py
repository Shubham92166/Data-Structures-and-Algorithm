#Given an integer array A of size N. You have to generate it's all subarrays having a size greater than 1.
#Then for each subarray, find Bitwise XOR of its maximum and second maximum element.
#Find and return the maximum value of XOR among all subarrays.

def solve(A):
    stack = []
    maxXor = 0
    for i in range(len(A)):
        while stack:
            maxXor = max(maxXor, A[stack[-1]] ^ A[i])
            if A[stack[-1]] > A[i]:
                break
            stack.pop()
        stack.append(i)
    return maxXor

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[2, 3, 1, 4], [1,3]

print(solve([2, 3, 1, 4]))
print(solve([1,3]))
