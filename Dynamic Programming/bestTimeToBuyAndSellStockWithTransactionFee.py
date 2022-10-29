def maxProfit(prices, fee):
    dp = [[-1]*2 for i in range(len(prices))] 
    return helper(prices, 0, 1, len(prices), dp, fee)

def helper(prices, i, canBuy, n, dp, fee):
    if i == n:
        return 0
    
    if dp[i][canBuy] != -1:
        return dp[i][canBuy]
    
    if canBuy == 1:
        dp[i][canBuy] = max(-prices[i]+helper(prices, i+1, 0, n, dp, fee), helper(prices, i+1, canBuy, n, dp, fee))
        return dp[i][canBuy]
        
    elif canBuy == 0:
        dp[i][canBuy] = max(prices[i]-fee+helper(prices, i+1, 1, n, dp, fee), helper(prices, i+1, canBuy, n, dp, fee))
        return dp[i][canBuy]
    
#Complexity:
#Time: O(n)
#Space: O(n*2) ==> O(n)

#Test Cases:
#[1,3,2,8,4,9], 2
#[1,3,7,5,10,3], 3

print(maxProfit([1,3,2,8,4,9], 2))
print(maxProfit([1,3,7,5,10,3], 3))

#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/