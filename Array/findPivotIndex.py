def pivotIndex(nums):
    PS =[0]*len(nums)
    PS[0] = nums[0]
    n = len(nums)
    for i in range(1, len(nums)):
        PS[i] = PS[i-1] + nums[i]
    for i in range(len(nums)):
        if i == 0:
            left = 0
        else:
            left = PS[i-1]
        right = PS[n-1] - PS[i]
        if left == right:
            return i
    return -1

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1,7,3,6,5,6], [1,2,3], [2,1,-1]

print(pivotIndex([1,7,3,6,5,6]))
print(pivotIndex( [1,2,3]))
print(pivotIndex([2,1,-1]))

#Link: https://leetcode.com/problems/find-pivot-index/