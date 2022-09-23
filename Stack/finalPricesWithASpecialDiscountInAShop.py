def finalPrices(prices):
    stack = []
    ans = []
    for i in range(len(prices)-1, -1, -1):
        while stack and stack[-1] > prices[i]:
            stack.pop()
        
        if stack:
            ans.append(prices[i] - stack[-1])
        else:
            ans.append(prices[i])
        
        stack.append(prices[i])
    
    return ans[::-1]

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[8,4,6,2,3], [1,2,3,4,5], [10,1,1,6]

print(finalPrices([8,4,6,2,3]))
print(finalPrices([1,2,3,4,5]))
print(finalPrices([10,1,1,6]))

#Link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/