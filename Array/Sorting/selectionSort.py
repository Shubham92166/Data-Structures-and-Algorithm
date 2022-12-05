def selectionSort(A,n):
    for i in range(0, n):
        minIndex = i
        for j in range(i+1, n):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]
    return A

#Complexity:
#Time: O(n^2)
#Space: O(1)

#Test Cases:
#[4, 1, 3, 9, 7], 5
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10

print(selectionSort([4, 1, 3, 9, 7], 5))
print(selectionSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10))

#Link: https://practice.geeksforgeeks.org/problems/selection-sort/1