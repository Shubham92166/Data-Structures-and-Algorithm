def subarraySum(A):
    sum = 0
    n = len(A)
    for i in range(len(A)):
        sum += (i+1)*(n-i)*A[i]
    return sum

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1, 2, 3], [2, 1, 3]

print(subarraySum([1, 2, 3]))
print(subarraySum([2, 1, 3]))

#Link: https://www.geeksforgeeks.org/sum-of-all-subarrays/