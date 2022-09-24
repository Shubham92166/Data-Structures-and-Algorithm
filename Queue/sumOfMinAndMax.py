import collections
class Solution:
  
    def solve(self, A, B):
        dq1 = collections.deque()
        ans = 0
        dq2 = collections.deque()
       
        for i in range(B):
            while dq1 and dq1[-1] < A[i]:
                dq1.pop()
                
            dq1.append(A[i])

        for i in range(B):
            while dq2 and dq2[-1] > A[i]:
                dq2.pop()
                
            dq2.append(A[i])
        
        ans += dq1[0]+dq2[0]

        for i in range(B, len(A)):
            if dq1[0] == A[i-B]:
                popped = dq1.popleft()
                
            
            while dq1 and dq1[-1] < A[i]:
                dq1.pop()
           
            dq1.append(A[i])
            if dq2[0] == A[i-B]:
                dq2.popleft()
                
            
            while dq2 and dq2[-1] > A[i]:
                dq2.pop()
           
            dq2.append(A[i])
            
            ans += dq1[0]+dq2[0]
        return ans % ((10**9)+7)

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[2, 5, -1, 7, -3, -1, -2], 4
#[2, -1, 3], 2

sol = Solution()

print(sol.solve([2, 5, -1, 7, -3, -1, -2], 4))
print(sol.solve([2, -1, 3], 2))