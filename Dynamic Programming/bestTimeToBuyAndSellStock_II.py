#Method-1: Using Top-down approach + Dp
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
#Space: O(n*2) ===> O(n)

#Run:
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))

#Method-2: Using Bottom-up approach + Dp

def maxProfit(prices):
    dp = [[0]*2 for i in range(len(prices)+1)] 
    return helper(prices, len(prices), dp)

def helper(prices, n, dp):
    for i in range(n-1, -1, -1):
        for canBuy in range(2):
            if canBuy:
                dp[i][canBuy] = max(-prices[i] + dp[i+1][0], dp[i+1][canBuy])
            else:
                dp[i][canBuy] = max(prices[i] + dp[i+1][1], dp[i+1][canBuy])
    
    return dp[0][-1]

#Complexity:
#Time: O(n)
#Space: O(n*2) ===> O(n)

#Run:
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))

#Method-3: Using Bottom-up approach + Space optimization

def maxProfit(prices): 
    return helper(prices, len(prices))

def helper(prices, n):
    prev = [0]* (n+1)
    for i in range(n-1, -1, -1):
        cur = [0]* (n+1)
        for canBuy in range(2):
            if canBuy:
                cur[canBuy] = max(-prices[i] + prev[0], prev[canBuy])
            else:
                cur[canBuy] = max(prices[i] + prev[1], prev[canBuy])
        
        prev = cur

    return cur[1]

#Complexity:
#Time: O(n)
#Space: O(n*2) ===> O(n)

#Run:
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))

#Test Cases:
#[7,1,5,3,6,4], [1,2,3,4,5], [7,6,4,3,1]

#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/