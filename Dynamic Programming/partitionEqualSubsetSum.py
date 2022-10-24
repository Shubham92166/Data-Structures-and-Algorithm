def canPartition(nums):
    totalSum = sum(nums)
    if totalSum % 2 != 0:
        return False
    dp = {}
    return helper(nums, totalSum//2, 0, len(nums), 0, dp)

def helper(nums, target, i, n, sum, dp):
    if i == n:
        if sum == target:
            return True
        return False
    
    if sum > target:
        return False
    
    if (i, sum) in dp:
        return dp[(i, sum)]
    
    val = helper(nums, target, i+1, n, sum + nums[i], dp) or helper(nums, target, i+1, n, sum, dp)
    dp[(i, sum)] = val
    
    return dp[(i, sum)]

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1,5,11,5], [1,2,3,5]

print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))

#Link: https://leetcode.com/problems/partition-equal-subset-sum/