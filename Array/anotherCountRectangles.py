def solve(A, B):
    n = len(A)
    i, j = 0, n-1
    count = 0
    while i < n and j >= 0:
        if A[i]*A[j] < B:
            count += (j+1)
            i += 1 
        else:
            j -= 1
    return count % 1000000007

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1, 2], 5
#[1, 2], 1
#[1, 2, 3, 4, 5], 5)

print(solve([1, 2], 5))
print(solve([1, 2], 1))
print(solve([1, 2, 3, 4, 5], 5))


