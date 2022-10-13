def binarysearch(arr, n, k): 
    l = 0
    r = n-1
    while(l <= r):
        mid = (l+r)//2
        if(arr[mid] == k):
            return mid
        elif(arr[mid] < k):
            l = mid+1
        else:
            r = mid-1
    return -1 

#Test Case: 
# [11, 22, 33, 44, 55], 1 
# [1,2,3,4,5], 4

#Complexity: 
#Time: O(log n)
#Space: O(1)

nums1=[11, 22, 33, 44, 55]
nums2= [1,2,3,4,5]

print(binarysearch(nums1, len(nums1), 1 ))
print(binarysearch(nums2, len(nums2), 4))