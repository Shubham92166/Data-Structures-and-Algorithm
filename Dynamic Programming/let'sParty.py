def solve(A):
    dp = [-1]*(A+1)
    dp[0] = dp[1] = 1
    return helper(A, dp) % 10003

def helper(A, dp):
    for i in range(2, A+1):   
        ans1 = dp[i-1] % 10003
        ans2 = ((i-1) * dp[i-2]) % 10003
        dp[i] = (ans1 + ans2) % 10003
    
    return dp[A] % 10003

#Complexity:
#Time: O(A)
#Space: O(A)

#Test Cases:
#3, 5, 17

print(solve(3))
print(solve(5))
print(solve(17))

#Link: https://www.geeksforgeeks.org/number-of-ways-to-pair-people/