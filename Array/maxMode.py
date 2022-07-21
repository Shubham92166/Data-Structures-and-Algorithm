import math
def solve(A):
    maxEle = max(A)
    ele = A[0]
    diff = math.inf
    for i in A:
        if i != maxEle and abs(i-maxEle) < diff:
            ele = i
            diff = abs(i-maxEle)
    if ele != maxEle:
        return ele
    return 0 

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1, 2, 44, 3], [2, 6, 4]

print(solve([2, 6, 4]))
print(solve([1, 2, 44, 3]))
