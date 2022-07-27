#Method-1:

#Approach: First finding the peak element and it's index so that we can search the 1 half of the array and thus reducing the time complexity to log(n)
#After finding the peak element and index, searching for the element in first half i.e, 0 to peakIndex which is sorted in ascending order. If it exists in the
#first half then simply return it.
#Else, search in second half i.e from peakIndex+1 to n-1 which is sorted in descending order. if it exists there then return peakIndex+index+1. Because the index retured from
#from the binary search is with repect to the second hlf so, we need to add the peakIndex because we ignored the first half and that would
#be the overall index
#If it doesn't exist in second half as well then we can say that the element is not present in the array and can return -1.

#So, in first case, we might end up in searching both the halves. Thus, our complexity would be log(n)+log(n) = 2log(n) = log(n)

def method1(A, B):
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

#To find peak element and it's index
    
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

 #To find the element in first half
    
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

#To find the element in second half

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

#Method-2:

#Optimization: Instead of having two different Binary search function for ascending and descending order array, we can merge them and create
#one single function and based on condition that whether the array is ascending or descending we will move l and r. Thus, reducing the
#number of functions. The overall approach and complexity remains same

def method2(A, B):
    reversed = False
    peakIndex, peakEle = findPeak(A)
    index1 = BS(A[:peakIndex+1], B, reversed = False)
    if index1 != -1:
        return index1
    else:
        if peakIndex < len(A):
            index2 = BS(A[peakIndex+1:], B, reversed = True)
            if index2 != -1:
                return peakIndex+index2+1
            else:
                return index2

def BS(A, B, reversed):
    l, r = 0, len(A)-1
    while l <= r:
        mid = l+(r-l)//2
        if A[mid] == B:
            return mid
        elif reversed == False:
            if A[mid] < B:
                l = mid+1
            else:
                r = mid-1
        elif reversed == True:
            if A[mid] < B:
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

print(method1([5, 6, 7, 8, 9, 10, 3, 2, 1], 30))
print(method1([3, 9, 10, 20, 17, 5, 1], 20))

print(method2([5, 6, 7, 8, 9, 10, 3, 2, 1], 30))
print(method2([3, 9, 10, 20, 17, 5, 1], 20))

#Link: https://www.geeksforgeeks.org/find-element-bitonic-array/