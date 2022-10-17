#Method-1: Using Top-down approach + Memoization

def rob(nums):
    n = len(nums)
    dp = [-1]*(n+1)
    return helper(nums, 0, n, dp)

def helper(nums, i, n, dp):
    if i >= n:
        return 0
    
    if dp[i] != -1:
        return dp[i]
    
    dp[i] = max(nums[i]+helper(nums, i+2, n, dp), helper(nums, i+1, n, dp))
    return dp[i]

#Time: O(n)
#Spaace: O(n)

#Run:
print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
print(rob([1]))
print(rob([1,2]))
print(rob([5,4,8,25,15,3,46,312,86,126,74,345]))

#Method-2: Using Bottom-up approach + Tabulation

def rob(nums):
    n = len(nums)
    dp = [0]*(n+2)
    return helper(nums, 0, n, dp)

def helper(nums, i, n, dp):
    for i in range(n-1, -1, -1):
        dp[i] = max(nums[i] + dp[i+2], dp[i+1])
    return dp[0]

#Complexity:
#Time: O(n)
#Space: O(n)

#Run:
print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
print(rob([1]))
print(rob([1,2]))
print(rob([5,4,8,25,15,3,46,312,86,126,74,345]))

#Method-3: Using Bottom-up approach + space optimization

def rob(nums):
    n = len(nums)
    return helper(nums, n)

def helper(nums, n):
    first = 0
    second = 0
    for i in range(n-1, -1, -1):
        first, second = max(nums[i] + second, first), first
        
    return first

#Complexity:
#Time: O(n)
#Space: O(1)

#Run:
print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))
print(rob([1]))
print(rob([1,2]))
print(rob([5,4,8,25,15,3,46,312,86,126,74,345]))

#Tes Cases:
#[1,2,3,1], [2,7,9,3,1], [1], [1,2], [5,4,8,25,15,3,46,312,86,126,74,345]

#Link: https://leetcode.com/problems/house-robber/
