def quickSort(arr,low,high):
        if(low < high):
            pivot = partition(arr, low, high)
            quickSort(arr, low, pivot-1)
            quickSort(arr, pivot+1, high)
        return arr
    
def partition(A, low, high):
    pivot = A[low]
    i = low+1
    j = high
    while(i <= j):
        if A[i] <= pivot:
            i += 1
        elif A[j] > pivot:
            j -= 1
        else:
            A[i], A[j] = A[j], A[i]
    A[j], A[low] = A[low], A[j]
    return j

#Complexity:
#Time: O(N^2)
#Space: O(1)

#Test Cases:
#[2, 1, 6, 10, 4, 1, 3, 9, 7]

arr = [2, 1, 6, 10, 4, 1, 3, 9, 7]
n = len(arr)
print(quickSort(arr, 0, n-1))