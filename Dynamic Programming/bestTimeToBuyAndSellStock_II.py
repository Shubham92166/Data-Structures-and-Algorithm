def maxProfit(prices):
    dp = [[-1]*2 for i in range(len(prices))] 
    return helper(prices, 0, 1, len(prices), dp)

def helper(prices, i, canBuy, n, dp):
    if i == n:
        return 0
    
    if dp[i][canBuy] != -1:
        return dp[i][canBuy]
    
    if canBuy == 1:
        dp[i][canBuy] = max(-prices[i]+helper(prices, i+1, 0, n, dp), helper(prices, i+1, canBuy, n, dp))
        return dp[i][canBuy]
        
    elif canBuy == 0:
        dp[i][canBuy] = max(prices[i]+helper(prices, i+1, 1, n, dp), helper(prices, i+1, canBuy, n, dp))
        return dp[i][canBuy]

#Complexity:
#Time: O(n)
#Space: O(2*n) ===> O(n)

#Test Cases:
#[7,1,5,3,6,4], [1,2,3,4,5], [7,6,4,3,1]

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))

#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/