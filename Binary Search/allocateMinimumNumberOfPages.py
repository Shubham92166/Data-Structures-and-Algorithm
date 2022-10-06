import math
def findPages(A, M):
    l = max(A)
    r = sum(A)
    
    if len(A) < M:
        return -1 
    ans = math.inf
    while l <= r:
        mid = l+(r-l)//2
        count = checkStudents(A, mid)

        if count > M:
            l = mid+1
        else:
            ans = min(ans, mid)
            r = mid-1 
    return ans

def checkStudents(A, target):
    sum = A[0]
    count = 1
    for i in range(1, len(A)):
        if sum + A[i] > target:
            sum = 0
            count += 1   
        sum += A[i]
    return count

#Complexity:
#Time: O(n logn)
#Space: O(1)

#Test Cases:
#[12,34,67,90], 2
#[15,17,20], 2

print(findPages([12,34,67,90], 2))
print(findPages([15,17,20], 2))

#Link: https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1