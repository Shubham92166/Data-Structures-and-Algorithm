def solve(A, B, C, D):
    dp = [[None]*(D+1) for i in range(len(A)+1)]

    return helper(A, B, C, D, 0, dp, len(A))
    
def helper(A, B, C, D, i, dp, n):
    if i ==  n:
        return 0

    ans1, ans2 = 0, 0

    if dp[i][D] != None:
        return dp[i][D]

    if C[i] <= D:
        ans1 = A[i]*B[i] + helper(A, B, C, D-C[i], i, dp, n)

    ans2 = helper(A, B, C, D, i+1, dp, n)

    dp[i][D] = max(ans1, ans2)

    return dp[i][D]

#Complexity:
#Time: O(n*D)
#Space: O(n*D)
#Where n is the length of A

#Test Cases:
#[1, 2, 3], [2, 2, 10], [2, 3, 9], 8
#[2], [5], [10], 99

print(solve([1, 2, 3], [2, 2, 10], [2, 3, 9], 8))
print(solve([2], [5], [10], 99))