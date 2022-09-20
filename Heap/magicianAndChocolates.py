from heapq import *

class Solution:
    def nchoc(self, A, B):
        heap = []
        heapify(heap)
        for i in B:
            heappush(heap, (-1)*i)
        total = 0
        for i in range(A):
            ele = heappop(heap)
            total += ele*(-1)
            heappush(heap, int(ele/2))
        return total % ((10**9)+7)

#Complexity:
#Time: O(n + mlogn)
#Space: O(n)

#Test Cases:
#3, [6, 5]
#5, [2, 4, 6, 8, 10]

sol = Solution()

print(sol.nchoc(3, [6, 5]))
print(sol.nchoc(5, [2, 4, 6, 8, 10]))

#Link: https://www.interviewbit.com/problems/magician-and-chocolates/