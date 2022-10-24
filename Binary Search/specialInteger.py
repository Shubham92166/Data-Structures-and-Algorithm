def solve(A, B):
    l, r = 0, len(A)
    while l <= r:
        mid = l + (r-l)//2 
        if is_Valid(A, mid, B):
            l = mid+1
        else:
            r = mid-1
    return l-1
    
def is_Valid(A, k, B):
    sum = 0
    for i in range(len(A)):
        sum += A[i]
        if i >= k:
            sum -= A[i-k]
        if sum > B:
            return False
    return True

#Complexity:
#Time: O(nlog n)
#Space: O(1)

#Test Cases:
#[1, 2, 3, 4, 5], 10
#[5, 17, 100, 11], 130

print(solve([5, 17, 100, 11], 130))
print(solve([1, 2, 3, 4, 5], 10))