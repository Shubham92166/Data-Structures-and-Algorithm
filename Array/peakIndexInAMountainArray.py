def peakIndexInMountainArray(arr):
    l = 0
    n = len(arr)
    r = n-1
    while(l<=r):
        mid = (l+r)//2
        if mid > 0 and mid < len(arr)-1:
            if arr[mid-1] <= arr[mid] and arr[mid+1] <= arr[mid]:
                return mid
            elif arr[mid-1] > arr[mid]:
                r = mid-1
            else:
                l = mid + 1
        elif mid == 0:
            if n > 1 and arr[1] < arr[0]:
                return 0
            elif n > 1 and arr[1] > arr[0]:
                return 1
        elif mid == n-1:
            if arr[n-1] >= arr[n-2]:
                return n-1
            else:
                return n-2
    return -1

#Complexity:
#Time: O(log n)
#Space: O(1)

#Test Cases:
#[0,1,0], [0,2,1,0], [0,10,5,2], [3,4,5,1], [3,5,3,2,0]

print(peakIndexInMountainArray([3,5,3,2,0]))
print(peakIndexInMountainArray([0,1,0]))
print(peakIndexInMountainArray([0,2,1,0]))
print(peakIndexInMountainArray([0,10,5,2]))
print(peakIndexInMountainArray([3,4,5,1]))