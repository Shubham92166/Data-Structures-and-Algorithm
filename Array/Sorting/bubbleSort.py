def bubbleSort(A, n):
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if A[j+1] < A[j]:
                swapped = True
                A[j], A[j+1] = A[j+1], A[j]
        if not swapped:
            break
    return A

#Complexity:
#Time: O(N^2)
#Space: O(1)

#Test Case:
#Test Cases:
#[4,5,9,4,2,3,6,7]

print(bubbleSort([4,5,9,4,2,3,6,7], len([4,5,9,4,2,3,6,7])))