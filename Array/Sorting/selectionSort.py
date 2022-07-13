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
#[4,5,9,4,2,3,6,7]

print(selectionSort([4,5,9,4,2,3,6,7], len([4,5,9,4,2,3,6,7])))