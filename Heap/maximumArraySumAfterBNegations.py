from heapq import *
class Solution:
    
    def solve(self, A, B):
        heap = A 
        heapify(heap)

        for i in range(B):
            minEle = heappop(heap)
            heappush(heap, (-1)*minEle)
        
        return sum(heap)

#Complexity:
#Time: O(n logn + B logn)
#Space: O(n)

#Test Cases:
#[24, -68, -29, -9, 84], 4
#[57, 3, -14, -87, 42, 38, 31, -7, -28, -61], 10

sol = Solution()

print(sol.solve([24, -68, -29, -9, 84], 4))
print(sol.solve([57, 3, -14, -87, 42, 38, 31, -7, -28, -61], 10))

#Link: https://practice.geeksforgeeks.org/problems/maximize-sum-after-k-negations1149/1


