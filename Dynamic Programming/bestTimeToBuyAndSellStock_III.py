def maxProfit(prices):
    n = len(prices)
    return helper(prices, n)
              
def helper(prices, n):
    prev = [[0]*3 for j in range(3)]
    for i in range(n-1, -1, -1):
        cur = [[0]*3 for j in range(3)]
        for count in range(1, 3):
            for canBuy in range(2):  
                if canBuy:
                    profit = max(-prices[i] + prev[count][0], prev[count][canBuy])
                else:
                    profit = max(prices[i] + prev[count-1][1], prev[count][canBuy])
                cur[count][canBuy] = profit

        prev = cur
    
    return cur[2][1]

#Complexity:
#Time: O(n*2*2) ==> O(n)
#Space: O(3*3) ==> O(1)

#Test Cases:
#[3,3,5,0,0,3,1,4], [1,2,3,4,5], [7,6,4,3,1]

print(maxProfit([3,3,5,0,0,3,1,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))

#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/