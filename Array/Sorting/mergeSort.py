def mergeSort(arr, l, r):
    if l >= r:
        return 
    mid = l+(r-l)//2
    mergeSort(arr, l, mid)
    mergeSort(arr, mid+1, r)
    merge(arr, l, mid, r)
    return arr
            
def merge(A, start, mid, end):
    i = start
    j = mid+1
    temp = []
    while i <= mid and j <= end:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1
    while i <= mid:
        temp.append(A[i])
        i += 1

    while j <= end:
        temp.append(A[j])
        j += 1
    
    for i in range(start, end + 1):
        A[i] = temp[i-start]
    return A

#Complexity:
#Time: O(nlogn)
#Space: O(n)

#Test Cases:
#[4, 1, 3, 9, 7], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(mergeSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, len([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])-1))
print(mergeSort([4, 1, 3, 9, 7], 0, len([4, 1, 3, 9, 7])-1))