def tribonacci(n):
    dp = [-1] * (n+1)
    return ans(n, dp)

def ans(n, dp):
    if n <= 1:
        return n
    if n == 2:
        return 1

    if dp[n] != -1:
        return dp[n]

    ans1 = ans(n-1, dp)
    ans2 = ans(n-2, dp)
    ans3 = ans(n-3, dp)
        
    dp[n] = ans1+ans2+ans3
    
    return dp[n] 

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#4, 25

print(tribonacci(4))
print(tribonacci(25))

#Link: https://leetcode.com/problems/n-th-tribonacci-number/