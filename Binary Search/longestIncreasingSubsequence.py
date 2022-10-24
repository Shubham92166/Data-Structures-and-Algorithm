"""
Approach: 

Initially we create a temporary array and put the first element of the given array into the temporary array. We iterate over the given
array from the second element and check it's correct position using Binary search because all the elements in the temporary array are 
stored in a soted way. If the element is greater than the last element of the temporary array then we append it at the end else we 
insert it at it's correct position. At the end, the length of the temporary array will represent the LIS. So, return the length of 
temporary array
"""

def lengthOfLIS(nums):
    n = len(nums)
    temp = [nums[0]]
    length = 1
    
    for i in range(1, n):
        if nums[i] > temp[-1]:
            temp.append(nums[i])
            length += 1
        else:
            correctPos = findCorrectPos(temp, nums[i])
            temp[correctPos] = nums[i]
    
    return length

def findCorrectPos(nums, target):
    l = 0
    r = len(nums)-1
    
    while l <= r:
        mid = l + (r-l)//2
        
        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            r = mid - 1
        
        else:
            l = mid + 1
    
    return l

#Complexity:
#Time: O(n logn)
#Space: O(n)

#Test Cases:
#[10,9,2,5,3,7,101,18], [0,1,0,3,2,3], [7,7,7,7,7,7,7]

print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))

#Link: https://leetcode.com/problems/longest-increasing-subsequence/