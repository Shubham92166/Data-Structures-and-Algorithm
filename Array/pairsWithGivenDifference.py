def solve(A, B):
    if len(A) <= 1:
        return 0
    elif len(A) == 2:
        if  A[1]-A[0] == B:
            return 1
        else:
            return 0
    i = 0
    j = 0
    s = set()
    A.sort()
    while i < len(A) and j < len(A):
        diff = abs(A[i] - A[j]) 
        if diff < B:
            i += 1
        elif diff > B:
            j += 1
        elif diff == B:
            s.add((A[i], A[j]))
            i += 1
            j += 1
    return len(s)

#Complexity:
#Time: O(n logn)
#Space: O(n)

#Test Cases:
#[1, 1], 0
#[1, 2], 0
#[1, 5, 3, 4, 2], 3
#[8, 12, 16, 4, 0, 20], 4
#[1, 1, 1, 2, 2], 0
#[ 8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8, 10, 6, 5, 4, 2, 3 ], 3

print(solve([ 8, 5, 1, 10, 5, 9, 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3, 2, 7, 9, 6, 8, 7, 2, 9, 10, 3, 8, 10, 6, 5, 4, 2, 3 ], 3))
print(solve([1, 1], 0))
print(solve([1, 2], 0))
print(solve([1, 5, 3, 4, 2], 3))
print(solve([8, 12, 16, 4, 0, 20], 4))
print(solve([1, 1, 1, 2, 2], 0))