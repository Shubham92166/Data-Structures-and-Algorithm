import math

def minCostClimbingStairs(cost):
    ans = math.inf
    n = len(cost)
    dp = [None]* (n+1)
    for i in range(0, 2):
        ans = min(ans, helper(i, cost, n, dp))
    return ans
    
def helper(i, cost, n, dp):
    if i >= n:
        return 0
    
    if dp[i] != None:
        return dp[i]
    
    ans1 = helper(i+1, cost, n, dp) 
    ans2 = helper(i+2, cost, n, dp)
    
    dp[i] = cost[i] + min(ans1, ans2)
    return dp[i]

#Time: O(2*n) ==> O(n)
#Space: O(n)
#Where n is the length of the given array

#Test Cases:
#[10,15,20], [1,100,1,1,1,100,1,1,100,1]

print(minCostClimbingStairs([10,15,20]))
print(minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))

#Link: https://leetcode.com/problems/min-cost-climbing-stairs/