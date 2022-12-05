def searchInsert(nums, target):
    l, r = 0, len(nums)

    #Since the array is sorted. We need to check whether the last index value is grater than the target value. If it is then the 
    #correct position will the be last index+1

    if(nums[-1] < target):
        return len(nums)
    
    #If the first index value is smaller than the target value than the correct position will be first index i.e., 0

    elif(nums[0] > target):
        return 0
    
    #If the above conditions fail then the correct position will be somewhere within the first and last index. Since the array 
    #is sorted, we can find the correct index using binary search

    else:
        while(l <= r):
            mid = (l+r)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                r = mid-1
            else:
                l = mid+1
    return l

#Test Cases: 
#[1,3,5,6], 5
#[1,3,5,6], 2
#[1,3,5,6], 7

#Complexity:
#Time: O(log n)
#Space: O(1)

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))

#Link: https://leetcode.com/problems/search-insert-position/


