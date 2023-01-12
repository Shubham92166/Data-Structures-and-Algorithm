from heapq import *
import math

def maxKelements(nums, k):
    heap = []
    heapify(heap)
    
    score = 0
    
    for num in nums:
        heappush(heap, -num)
    
    while k:
        maxEle = -heappop(heap)
        
        score += maxEle
        
        heappush(heap, -math.ceil(maxEle/3))
        
        k -= 1
    
    return score
        
#Complexity:
#Time: O(n logn)
#Space: O(n)

#Test Cases:
#[10,10,10,10,10], 5
#[1,10,3,3,3], 3

print(maxKelements([10,10,10,10,10], 5))
print(maxKelements([1,10,3,3,3], 3))

#Link: https://leetcode.com/problems/maximal-score-after-applying-k-operations/