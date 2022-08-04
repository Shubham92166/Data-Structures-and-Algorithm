import math
def minimumInteger(A):
    sumOfArray = sum(A)
    N = len(A)
    val = math.ceil(sumOfArray/N)
    minVal = math.inf
    for ele in A:
        if val <= ele:
            minVal = min(minVal, ele)
    return minVal

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1, 3, 2], [3]

print(minimumInteger([1, 3, 2]))
print(minimumInteger([3]))

#Link: https://practice.geeksforgeeks.org/contest/interview-series-56/problems/#