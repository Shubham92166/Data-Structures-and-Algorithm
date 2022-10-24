from heapq import *
def solve(A, B):
    ans = 0
    heap = A.copy()
    heapify(heap)
    while heap:
        ele = heappop(heap)
        if ele > B:
            break
        if ele <= B:
            eat = (ele)//2
            ans += eat
            if heap:
                minEle = heappop(heap)
                minEle+= (ele-eat)
                heappush(heap, minEle)
    return ans

#Complexity:
#Time: O(n logn)
#Space: O(n)

#Test Cases:
#[3, 2, 3], 4
#[1, 2, 1], 2

print(solve([3, 2, 3], 4))
print(solve([1, 2, 1], 2))