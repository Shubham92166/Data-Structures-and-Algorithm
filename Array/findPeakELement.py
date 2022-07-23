from gettext import find


def findPeakElement(arr):
    l = 0
    n = len(arr)
    r = n-1
    if n == 1:
        return 0
    while(l<=r):
        mid = (l+r)//2
        if mid > 0 and mid < n-1:
            if arr[mid-1] < arr[mid] and arr[mid+1] < arr[mid]:
                return mid
            elif arr[mid-1] > arr[mid]:
                r = mid-1
            else:
                l = mid + 1
        elif mid == 0:
            if arr[0] > arr[1]:
                return 0
            elif arr[0] < arr[1]:
                return 1

        elif mid == n-1:
            if arr[n-1] > arr[n-2]:
                return n-1
            else:
                return n-2
    return -1

#Complexity:
#Time: O(log n)
#Space: O(1)

#Test cases:
#[1,2,3,1], [2,1], [1,2], [2], [1,2,1,3,5,6,4]

print(findPeakElement([1,2,1,3,5,6,4]))
print(findPeakElement([2]))
print(findPeakElement([[1,2]]))
print(findPeakElement([2,1]))
print(findPeakElement([1,2,3,1],))