import collections
def maxSlidingWindow(A, B):
    deq = collections.deque()
    ans = []
    for i in range(B):
        while deq and deq[-1] < A[i]:
            deq.pop()
        deq.append(A[i])
    ans.append(deq[0])
    
    for i in range(B, len(A)):
        if deq[0] == A[i-B]:
            deq.popleft()
        
        while deq and deq[-1] < A[i]:
            deq.pop()
        
        deq.append(A[i])
        ans.append(deq[0])
    
    return ans

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1,3,-1,-3,5,3,6,7], 3
#[1], 1
#[1,-1], 1

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow([1], 1))
print(maxSlidingWindow([1,-1], 1))

#Link: https://leetcode.com/problems/sliding-window-maximum/