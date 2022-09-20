from heapq import *

def solve(A):
    heap = A 
    heapify(heap)
    total = 0
    if len(heap) == 1:
        return 0
    for i in range(len(A)):
        if len(heap) == 1:
            break
        first = heappop(heap)
        second = heappop(heap)
        sum = first + second
        heappush(heap, sum)
        total += sum
    return total

#Complexity:
#Time: O(n logn)
#Space: O(n)

#Test Cases:
#[1, 2, 3, 4, 5], [5, 17, 100, 11]

print(solve([1, 2, 3, 4, 5]))
print(solve([5, 17, 100, 11]))

#Link: https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1