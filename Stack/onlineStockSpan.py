class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price):
        count = 1
        while self.stack and price >= self.stack[-1][0]:
            count += self.stack.pop()[1]

        self.stack.append([price, count])
        
        return count

#Complexity:
#Time: O(q)
#Space: O(q)
#where q is the no. of queries

#Test Cases:
#["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
#[[], [100], [80], [60], [70], [60], [75], [85]]

#Link: https://leetcode.com/problems/online-stock-span/