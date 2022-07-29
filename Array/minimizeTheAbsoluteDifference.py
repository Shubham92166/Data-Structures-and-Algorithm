import math
def solve(A, B, C):
    i, j, k = 0, 0, 0
    ans = math.inf
    while i < len(A) and j < len(B) and k < len(C):
        ans = min(ans, abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k])))
        if A[i] <= B[j] and A[i] <= C[k]:
            i += 1
        elif B[j] <= A[i] and B[j] <= C[k]:
            j += 1
        elif C[k] <= A[i] and C[k] <= B[j]:
            k += 1
    return ans

#Complexity:
#Time: O(n) #Three arrays are of same length
#Space: O(1)

#Test Cases:
#[1, 4, 5, 8, 10], [6, 9, 15], [2, 3, 6, 6]
#[5, 8, 10, 15], [6, 9, 15, 78, 89], [2, 3, 6, 6, 8, 8, 10]

print(solve([1, 4, 5, 8, 10], [6, 9, 15], [2, 3, 6, 6]))
print(solve([5, 8, 10, 15], [6, 9, 15, 78, 89], [2, 3, 6, 6, 8, 8, 10]))

#Link: https://www.geeksforgeeks.org/minimize-maxai-bj-ck-minai-bj-ck-three-different-sorted-arrays/