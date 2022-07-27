def pickFromBothSides(A, B):
    maxSum = 0
    sum = 0
    for i in range(B):
        sum += A[i]
    maxSum = sum
    leftIndex = B-1
    rightIndex = len(A)-1
    while leftIndex >= 0:
        sum -= A[leftIndex]
        leftIndex -= 1
        sum += A[rightIndex]
        rightIndex -= 1
        if sum > maxSum:
            maxSum = sum
    return maxSum

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[5, -2, 3 , 1, 2], 3
#[1, 2], 1

print(pickFromBothSides([1, 2], 1))
print(pickFromBothSides([5, -2, 3 , 1, 2], 3))

#Link: https://www.interviewbit.com/problems/pick-from-both-sides/
