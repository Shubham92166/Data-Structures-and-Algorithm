import sys
sys.setrecursionlimit(10**9)
def solve(A):
    return mergeSort(A, 0, len(A)-1) % ((10**9)+7)

def mergeSort(A, start, end):
    if start >= end:
        return 0
    mid = start + (end-start)//2
    left = mergeSort(A, start, mid) % ((10**9)+7)
    right = mergeSort(A, mid+1, end) % ((10**9)+7)
    return (left + right + merge(A, start, mid, end)) % ((10**9)+7)

def merge(A, start, mid, end):
    i = start 
    j = mid+1
    T = []
    inversions = 0
    while i <= mid and j <= end:
        if A[i] <= A[j]:
            T.append(A[i])
            i += 1
        else:
            T.append(A[j])
            inversions += mid-i+1
            j += 1

    while i <= mid:
        T.append(A[i])
        i += 1
    while j <= end:
        T.append(A[j])
        j += 1
    for i in range(start, end+1):
        A[i] = T[i-start]
    return inversions

#Complexity:
#Time: O(nlogn)
#Space: O(nlogn)

#Test Cases:
#[3, 2, 1], [1,2,3]

print(solve([3, 2, 1]))
print(solve([1,2,3]))
