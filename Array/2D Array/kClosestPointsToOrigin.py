#Method-1: Using Array:

import math
def kClosest(points, k):
    ans = []
    allDistances = []
    
    for point in points:
        distance = math.sqrt(pow(point[0], 2) + pow(point[1], 2))
        allDistances.append((distance, point))
    
    allDistances.sort(key = lambda x : x[0])
    
    for closestPoint in allDistances[:k]:
        ans.append(closestPoint[1])
    
    return ans

#Complexity:
#Time: O(n logn)
#Space: O(n)

#Run:
print(kClosest([[1,3],[-2,2]], 1))
print(kClosest([[3,3],[5,-1],[-2,4]], 2))

#MEthod-2: Using Heap:

from heapq import *

def solve(A, B):
    heap = []
    for i in A:
        distance = math.sqrt((i[0]**2)+(i[1]**2))
        pair = (distance, i)
        heappush(heap, pair)

    ans = []
    for i in range(B):
        ele = heappop(heap)
        ans.append(ele[1])
        
    return ans

#Complexity:
#Time: O(n logn)
#Space: O(n)


#Test Cases:
#[[1,3],[-2,2]], 1
#[[3,3],[5,-1],[-2,4]], 2

#Run:
print(solve([[1,3],[-2,2]], 1))
print(solve([[3,3],[5,-1],[-2,4]], 2))

#Link: https://leetcode.com/problems/k-closest-points-to-origin/

