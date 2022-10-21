import math
def coinChange(coins, amount):
    if amount == 0:
        return 0
    dp = [[None]*(amount+1) for i in range(len(coins)+1)]
    ans = helper(coins, amount, len(coins)-1, dp)
    if ans == math.inf:
        return -1
    return ans

def helper(coins, target, i, dp):
    if i == -1:
        if target == 0:
            return 0
        return math.inf
    
    if target == 0:
        return 0
    
    if dp[i][target] != None:
            return dp[i][target]
    
    take = math.inf
    if target - coins[i] >= 0:
        take = 1 + helper(coins, target - coins[i], i, dp)
    skip = helper(coins, target, i-1, dp)
    
    dp[i][target] = min(take, skip)
    return dp[i][target]

#Complexity:
#Time: O(n*m)
#Space: O(n*m)

#Test Cases:
#[1,2,5], 11
#[2], 3
#[1], 0

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))
print(coinChange([1], 0))

#Link: https://leetcode.com/problems/coin-change/