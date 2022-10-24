from heapq import *

def solve(A):
    ans = [-1]* len(A)
    heap = []

    for i in range(len(A)):
        if i < 2:
            heappush(heap, (-1)*A[i])
            
        else:
            third = heappush(heap, (-1)*A[i])
            first = heappop(heap)
            second = heappop(heap)
            third = heappop(heap)
            
            ans[i] = (-1)*first*second*third
            heappush(heap, first)
            heappush(heap, second)
            heappush(heap, third)
    
    return ans

#Complexity:
#Time: O(n logn)
#Space: O(n)

#Test Cases:
#[1, 2, 3, 4, 5], [10, 2, 13, 4]

print(solve([1, 2, 3, 4, 5]))
print(solve([10, 2, 13, 4]))