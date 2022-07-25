import math
def findMinXor(A):
    minVal = math.inf
    A.sort()
    for i in range(len(A)-1):
        minVal = min(minVal, A[i] ^ A[i+1])
    return minVal

#Complexity:
#Time: O(nlog n)
#Space: O(n)

#Test Cases:
#[2, 6, 4 , 12], [0, 2, 5, 7], [0, 4, 7, 9]

print(findMinXor([0, 4, 7, 9]))
print(findMinXor([0, 2, 5, 7]))
print(findMinXor([2, 6, 4 , 12]))

#Link: https://www.geeksforgeeks.org/minimum-xor-value-pair/
