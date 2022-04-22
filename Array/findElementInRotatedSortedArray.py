#Approach-1: USing Binary Search

def searchInRotatedSortedArray(A, key):
        l=0
        r=len(A)-1
        while(l<=r):
            mid=(l+r)//2
            if(A[mid]==key):
                return mid
            if(A[l]<=A[mid]):
                if(A[l]<=key and A[mid]>=key):
                    r=mid-1
                else:
                    l=mid+1
            else:
                if(A[mid]<key and A[r]>=key):
                    l=mid+1
                else:
                    r=mid-1
        return -1

#Test Case: [5, 6, 7, 8, 9, 10, 1, 2, 3], [3,1], [1,3]


#Complexity:O(log n)
#Time: O(1)

print(searchInRotatedSortedArray([5, 6, 7, 8, 9, 10, 1, 2, 3], 10))
print(searchInRotatedSortedArray([5, 6, 7, 8, 9, 10, 1, 2, 3], 15))
print(searchInRotatedSortedArray([3,1], 1))
print(searchInRotatedSortedArray([1,3], 1))
