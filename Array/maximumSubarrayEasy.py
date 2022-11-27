'''
You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous 
elements is maximum. But the sum must not exceed B.

Problem Constraints
1 <= A <= 103
1 <= B <= 109
1 <= C[i] <= 106
'''

def maxSubarray(A, B, C):
    maxSum = 0
    for i in range(A):
        sum = 0
        for j in range(i, A):
            sum += C[j]
            if sum <= B:
                if sum > maxSum:
                    maxSum = sum
            else:
                break
    return maxSum

#Complexity:
#Time: O(n^2)
#Space: O(1)

#Test Cases:
#5, 12, [2, 1, 3, 4, 5]
#3, 1, [2, 2, 2]

print(maxSubarray(5, 12, [2, 1, 3, 4, 5]))
print(maxSubarray(3, 1, [2, 2, 2]))