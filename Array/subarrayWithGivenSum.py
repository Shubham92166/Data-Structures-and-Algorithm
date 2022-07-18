def subarraySum(A, B):
    i = 0
    j = 0
    sum = 0
    while(i < len(A) and j < len(A)):
        if sum == B:
            return A[i:j]
        elif sum < B:
            sum += A[j]
            j += 1
        elif sum > B:
            sum -= A[i]
            i += 1
    if sum-A[i] == B:
        i += 1
        return A[i:j]    
    return [-1]

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1, 1000000000] ,1000000000
#[1, 2, 3, 4, 5], 5
#[5, 10, 20, 100, 105], 110

print(subarraySum([5, 10, 20, 100, 105], 110))
print(subarraySum([1, 2, 3, 4, 5], 5))
print(subarraySum([1, 1000000000] ,1000000000))
