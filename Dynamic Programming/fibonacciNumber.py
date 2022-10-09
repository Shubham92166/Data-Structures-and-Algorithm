def fib(n):
    dp = [-1 for i in range(n+1)]
    return fibonacci(n, dp)

def fibonacci(n, dp):
    if n <= 1:
        return n
    if dp[n-1] == -1:
        ans1 = fibonacci(n-1, dp)
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]
    if dp[n-2] == -1:
        ans2 = fibonacci(n-2, dp)
        dp[n-2] = ans2
    else:
        ans2 = dp[n-2]
    return ans1 + ans2
            
#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#2, 4, 30

print(fibonacci(2))
print(fibonacci(4))
print(fibonacci(30))

#Link: https://leetcode.com/problems/fibonacci-number/