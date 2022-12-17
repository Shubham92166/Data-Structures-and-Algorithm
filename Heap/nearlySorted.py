from heapq import *

def nearlySorted(a,n,k):
    nums = []
    heap = []
    heapify(heap)
    
    for index in range(n):
        heappush(heap, a[index])
        
        if index > k:
            nums.append(heappop(heap))
        
    while heap:
        nums.append(heappop(heap))
    
    return nums

#Complexity:
#Time: O(n logk)
#Space: O(k) if k == n then O(n)
#Where n is the length of the array

#Test Cases:
#[6,5,3,2,8,10,9], 7, 3
#[3,1,4,2,5], 5, 2

print(nearlySorted([6,5,3,2,8,10,9], 7, 3))
print(nearlySorted([3,1,4,2,5], 5, 2))

#Link: https://practice.geeksforgeeks.org/problems/nearly-sorted-1587115620/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article