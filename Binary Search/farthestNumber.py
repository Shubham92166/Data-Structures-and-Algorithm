def farNumber(A):
    N = len(A)
    suffix = [-1]*N
    suffix[-1] = A[-1]
    for i in range(N-2, -1, -1):
        suffix[i] = min(A[i], suffix[i+1])
    res =[-1]*N
    for i in range(N):
        l = i+1
        r = N-1
        ans = -1
        while l <= r:
            mid = l+(r-l)//2
            if suffix[mid] < A[i]:
                ans = mid
                l = mid+1
            else:
                r = mid-1
        res[i] = ans
    return res

#Complexity:
#Time: O(n logn)
#Space: O(1)

#Link: https://practice.geeksforgeeks.org/contest/interview-series-61/problems/#