from functools import lru_cache

#Method-1: Using Top down approach

def numDecodings(s):
        return helper(s, 0, len(s))

@lru_cache
def helper(s, i, n):
    if i == n:
        return 1
    if s[i] == "0":
        return 0
    
    if i < n-1 and int(s[i]+s[i+1]) <= 26:
        return helper(s, i+1, n) + helper(s, i+2, n)
    
    return helper(s, i+1, n)

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the length of the given string

#Run:
print(numDecodings("12"))
print(numDecodings("226"))
print(numDecodings("06"))
print(numDecodings("246541212464300000022464612"))
print(numDecodings("0021440004669"))
print(numDecodings("10000"))
print(numDecodings("0000"))
print(numDecodings("0"))
print(numDecodings("01"))

#Method-2: Using Bottom up approach

def numDecodings(s):
    dp = [0 for i in range(len(s)+1)]
    dp[-1] = 1
    return helper(s, 0, dp)
    

def helper(s, i, dp):
    for i in range(len(s)-1, -1, -1): 
        if s[i] == "0":
            dp[i] = 0
            continue
        
        if i < len(s)-1 and int(s[i]+s[i+1]) <= 26:
            dp[i] = dp[i+1] + dp[i+2]
        else:
            dp[i] = dp[i+1]
            
    return dp[0]

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the length of the given string

#Run: 
print(numDecodings("12"))
print(numDecodings("226"))
print(numDecodings("06"))
print(numDecodings("246541212464300000022464612"))
print(numDecodings("0021440004669"))
print(numDecodings("10000"))
print(numDecodings("0000"))
print(numDecodings("0"))
print(numDecodings("01"))

#Method-3: Using Bottom up approach + Space optimization

def numDecodings(s):   
    return helper(s, 0, 1, 0)
    

def helper(s, i, first, second):
    for i in range(len(s)-1, -1, -1): 
        cur = 0
        if s[i] == "0":
            first, second = cur, first
            continue
        
        if i < len(s)-1 and int(s[i]+s[i+1]) <= 26:
            cur = first + second
        else:
            cur = first
    
        first, second = cur, first
        
    return cur

#Complexity:
#Time: O(n)
#Space: O(1)
#where n is the length of the given string

#Run: 
print(numDecodings("12"))
print(numDecodings("226"))
print(numDecodings("06"))
print(numDecodings("246541212464300000022464612"))
print(numDecodings("0021440004669"))
print(numDecodings("10000"))
print(numDecodings("0000"))
print(numDecodings("0"))
print(numDecodings("01"))

#Test Cases:
#"12", "226", "06", "246541212464300000022464612", "0021440004669", "10000", "0000", "0", "01"


#Link: https://leetcode.com/problems/decode-ways/