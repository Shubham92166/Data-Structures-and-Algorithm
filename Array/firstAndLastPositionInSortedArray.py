def searchRange(nums, target):
        l = 0
        r = len(nums)-1
        ans = []
        while l <= r:
            mid = l +(r-l)//2
            if nums[mid] < target and (mid == 0 or nums[mid-1] < target):
                l = mid+1
            else:
                r = mid-1
        first = l

        l = first
        r = len(nums)-1
        while l <= r:
            mid = l +(r-l)//2
            if nums[mid] <= target:
                l = mid+1
            else:
                r = mid-1
        second = l-1
        if(first < len(nums) and nums[first]==target):
            if l > 0 and nums[second] == target:
                return [first, second]
        return [-1, -1]

#Complexity:
#Time: O(log n)
#Space: O(1)

#Test Cases:
#[5,7,7,8,8,10], 8
#[5,7,7,8,8,10], 6
#[], 0
#[1], 1
#[2], -2

print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 6))
print(searchRange([], 0))
print(searchRange([1], 1))
print(searchRange([2], -2))

#Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
