def climbStairs(n):
        dp = [-1]*n
        return climb(n, dp)
def climb(n, dp):
    if(n < 0):
        return 0
    if n == 1:
        return 1
    if(n == 2):
        return 2
    if dp[n-1] == -1:
        ans1 = climb(n-1, dp)
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]
    
    if dp[n-2] == -1:
        ans2 = climb(n-2, dp)
        dp[n-2] = ans2
    else:
        ans2 = dp[n-2]
    
    ans = ans1+ans2
    return ans

#Test Cases:
#1, 2, 16, 45

#Complexity:
#Time: 
#Space: 

print(climbStairs(1))
print(climbStairs(2))
print(climbStairs(16))
print(climbStairs(45))