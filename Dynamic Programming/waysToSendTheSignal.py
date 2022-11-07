'''
You are trying to send signals to aliens using a linear array of A laser lights. You don't know much about how the aliens are going to
percieve the signals, but what you know is that if two consecutive lights are on then the aliens might take it as a sign of danger and 
destroy the earth. Find and return the total number of ways in which you can send a signal without compromising the safty of the earth. 
Return the ans % 109 + 7.
'''

from sys import setrecursionlimit
setrecursionlimit(10**8)

def solve(A):
    dp = [-1]*A
    mod = 1000000007
    return (helper(0, A, dp, mod)) % mod
    
def helper(i, A, dp, mod):
    if i >= A:
        return 1

    if dp[i] != -1:
        return dp[i]

    dp[i] = (helper(i+2, A, dp, mod) % mod + helper(i+1, A, dp, mod) % mod) % mod
    
    return dp[i]

#Complexity:
#Time: O(A)
#Space: O(A)

#Test Cases:
#2, 3

print(solve(2))
print(solve(3))


