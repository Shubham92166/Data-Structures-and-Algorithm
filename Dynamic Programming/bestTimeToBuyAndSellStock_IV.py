def maxProfit(k, prices):
    n = len(prices)
    return helper(prices, n, k)
              

def helper(prices, n, k):
    prev = [[0]*3 for j in range(k+1)]
    for i in range(n-1, -1, -1):
        cur = [[0]*3 for j in range(k+1)]
        for count in range(1, k+1):
            for canBuy in range(2):  
                if canBuy:
                    profit = max(-prices[i] + prev[count][0], prev[count][canBuy])
                else:
                    profit = max(prices[i] + prev[count-1][1], prev[count][canBuy])
                cur[count][canBuy] = profit
        prev = cur
        
    return cur[k][1]

#Complexity:
#Time: O(n*k)
#Space: O(k*3) ==> O(k)

#Test Cases:
#2, [2,4,1]
#2, [3,2,6,5,0,3]

print(maxProfit(2, [2,4,1]))
print(maxProfit(2, [3,2,6,5,0,3]))

#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/