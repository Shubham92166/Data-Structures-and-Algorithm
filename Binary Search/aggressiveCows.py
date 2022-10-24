def isValid(A, B, expected_distance):
    i = 1
    prev = A[0]
    B -= 1
    n = len(A)
    while B > 0:
        while i < n and A[i]-prev < expected_distance:
            i += 1
        if i == n:
            return False
        prev = A[i]
        B -= 1
        i += 1
    return True

def aggressiveCows(A, B):
    A.sort()
    n = len(A)
    l, r = 1, (A[n-1]-A[0])//(B-1)
    while l <= r:
        mid = l+(r-l)//2
        if isValid(A, B, mid):
            l = mid+1
        else:
            r = mid-1
    return l-1

#Complexity:
#Time: O(n log((max(A)-min(A))/(B-1)) + n log(n)) # n is the size of A
#Space: O(1)

#Test Cases:
#[1, 2, 3, 4, 5], 3
#[1, 2], 2

print(aggressiveCows([1, 2], 2))
print(aggressiveCows([1, 2, 3, 4, 5], 3))