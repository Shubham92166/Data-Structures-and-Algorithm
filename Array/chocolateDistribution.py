import math
def chocolateDistribution(A, B):
    diff = math.inf
    if len(A) == 0 or B == 0:
        return 0
    A.sort()
    diff = (A[B-1]-A[0])
    for i in range(B, len(A)):
        diff = min(diff, A[i]-A[i-B+1])
    return diff

#Test case:
#[3, 4, 1, 9, 56, 7, 9, 12], 5

print(chocolateDistribution([3, 4, 1, 9, 56, 7, 9, 12], 5))