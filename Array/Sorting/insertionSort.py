def insertionSort(A, n):
    for i in range(1, n):
        j = i-1
        temp = A[i]
        while(j >= 0 and A[j] > temp):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = temp
    return A

#Complexity:
#Time: O(n^2)
#Space: O(1)

#Test Cases:
#[4,5,9,4,2,3,6,7]

print(insertionSort([4,5,9,4,2,3,6,7], len([4,5,9,4,2,3,6,7])))