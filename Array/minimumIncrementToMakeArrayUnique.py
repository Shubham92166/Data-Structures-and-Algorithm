def minIncrementForUnique(nums):
    nums.sort()
    lastMin = nums[0]
    steps = 0
    for index in range(1, len(nums)):
        if nums[index] <= nums[index-1]:
            steps = steps + (lastMin-nums[index]) + 1
            nums[index] += (lastMin-nums[index]) + 1
            lastMin = nums[index]
        else:
            lastMin = nums[index]
    return steps

#Complexity:
#Time: O(n logn)
#Space: O(1)

#Test Cases:
#[1,2,2], [3,2,1,2,1,7], [5,5,5,5,5,7,8,8,9,9,4,5,2,3,4,5,5,6,1,2,2,1,2,33,4,5,45,4,54,45,45,56,44]

print(minIncrementForUnique([1,2,2]))
print(minIncrementForUnique([3,2,1,2,1,7]))
print(minIncrementForUnique([5,5,5,5,5,7,8,8,9,9,4,5,2,3,4,5,5,6,1,2,2,1,2,33,4,5,45,4,54,45,45,56,44]))

#Link: https://leetcode.com/problems/minimum-increment-to-make-array-unique/