def rob(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [-1]*(n+1)
    first = helper(nums, 0, n-1, dp)
    dp = [-1]*(n+1)
    second = helper(nums, 1, n, dp)
    return max(first, second)

def helper(nums, i, n, dp):
    if i >= n:
        return 0

    if dp[i] != -1:
        return dp[i]

    dp[i] = max(nums[i]+ helper(nums, i+2, n, dp), helper(nums, i+1, n, dp))
    return dp[i]

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[2,3,2], [1,2,3,1], [1,2,3], [2]

print(rob([2,3,2]))
print(rob([1,2,3,1]))
print(rob([1,2,3]))
print(rob([2]))

#Link: https://leetcode.com/problems/house-robber-ii/
