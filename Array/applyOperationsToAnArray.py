def applyOperations(nums):
    n = len(nums)
    for i in range(n-1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0
    
    j = 0
    
    for i in range(n):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        
    return nums

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1,2,2,1,1,0]
#[0,1]

print(applyOperations([1,2,2,1,1,0]))
print(applyOperations([0,1]))

#Link: https://leetcode.com/problems/apply-operations-to-an-array/