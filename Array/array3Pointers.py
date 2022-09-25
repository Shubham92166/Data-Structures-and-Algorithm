import math

def minimize(A, B, C):
        i, j, k = 0, 0, 0
        n = len(A)
        ans = math.inf
        while i < len(A) and j < len(B) and k < len(C):
            val = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
            ans = min(ans, val)
            minValue = min(A[i], B[j], C[k])
            if A[i] == minValue:
                i += 1
            elif B[j] == minValue:
                j += 1
            else:
                k += 1
        return ans

#Complexity:
#Time: O(p+q+r)
#Space: O(1)

#Test Cases:
#[1, 4, 10], [2, 15, 20], [10, 12]
#[3, 5, 6], [2], [3, 4]

print(minimize([1, 4, 10], [2, 15, 20], [10, 12]))
print(minimize([3, 5, 6], [2], [3, 4]))

#Link: https://www.geeksforgeeks.org/find-three-closest-elements-from-given-three-sorted-arrays/