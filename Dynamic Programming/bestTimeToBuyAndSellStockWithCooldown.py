def maxProfit(prices):
    dp = [[-1]*2 for i in range(len(prices))] 
    return helper(prices, 0, 1, len(prices), dp)

def helper(prices, i, canBuy, n, dp):
    if i >= n:
        return 0
    
    if dp[i][canBuy] != -1:
        return dp[i][canBuy]
    
    if canBuy == 1:
        dp[i][canBuy] = max(-prices[i]+helper(prices, i+1, 0, n, dp), helper(prices, i+1, canBuy, n, dp))
        return dp[i][canBuy]
        
    elif canBuy == 0:
        dp[i][canBuy] = max(prices[i]+helper(prices, i+2, 1, n, dp), helper(prices, i+1, canBuy, n, dp))
        return dp[i][canBuy]

#Complexity:
#Time: O(n)
#Space: O(2*n) ===> O(n)

#Test Cases:
#[1,2,3,0,2], [1], [1,6,7,54,659,10,20,0,69,15,123,759,20,89]

print(maxProfit([1,2,3,0,2]))
print(maxProfit([1]))
print(maxProfit([1,6,7,54,659,10,20,0,69,15,123,759,20,89]))

#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/