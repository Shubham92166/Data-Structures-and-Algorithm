#Method-1:

def solve(A, B):
        peakIndex, peakEle = findPeak(A)
        index1 = BS1(A[:peakIndex+1], B)
        if index1 != -1:
            return index1
        else:
            if peakIndex < len(A):
                index2 = BS2(A[peakIndex+1:], B)
                if index2 != -1:
                    return peakIndex+index2+1
                else:
                    return index2

    
def findPeak(arr):
    l = 0
    n = len(arr)
    r = n-1
    while(l<=r):
        mid = (l+r)//2
        if (mid == 0 or arr[mid] >= arr[mid-1]) and (mid == n-1 or arr[mid] >= arr[mid+1]):
            return mid, arr[mid]
        elif mid > 0 and arr[mid-1] > arr[mid]:
            r = mid-1
        else:
            l = mid+1
    
def BS1(A, B):
    l, r = 0, len(A)-1
    while l <= r:
        mid = l+(r-l)//2
        if A[mid] == B:
            return mid
        elif A[mid] < B:
            l = mid+1
        else:
            r = mid-1
    return -1

def BS2(A, B):
    l, r = 0, len(A)-1
    while l <= r:
        mid = l+(r-l)//2
        if A[mid] == B:
            return mid
        elif A[mid] < B:
            r = mid-1
        else:
            l = mid+1
    return -1

#Complexity:
#Time: O(log n)
#Space: O(1)

#Test Cases:
#[3, 9, 10, 20, 17, 5, 1], 20
#[5, 6, 7, 8, 9, 10, 3, 2, 1], 30

print(solve([5, 6, 7, 8, 9, 10, 3, 2, 1], 30))
print(solve([3, 9, 10, 20, 17, 5, 1], 20))