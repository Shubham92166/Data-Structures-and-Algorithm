from heapq import *

def minimizeSum(N, arr):
    heap = arr
    heapify(arr)
    
    totalSum = 0
    while len(heap) > 1:
        first = heappop(heap)
        second = heappop(heap)
        
        sum = first + second
        
        heappush(heap, sum)
        
        totalSum += sum

    return totalSum

#Complexity:
#Time: O(n logn)
#Space: O(n)
#n is the size of the array

#Test Cases:
#4, [1, 4, 7, 10]
#5, [1, 3, 7, 5, 6]

print(minimizeSum(4, [1, 4, 7, 10]))
print(minimizeSum(5, [1, 3, 7, 5, 6]))

#Link: https://practice.geeksforgeeks.org/problems/86e609332c9ef4f6b8aa79db11a6c0808c4a1bca/1