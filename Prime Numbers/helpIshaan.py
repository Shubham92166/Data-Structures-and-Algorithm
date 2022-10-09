import math
def NthTer(N):
    ans1 = N
    ans2 = N
    if N == 1:
        return N

    while not isPrime(ans1) and not isPrime(ans2):
        ans1 -= 1
        ans2 += 1    
        
    return min(abs(N-ans1), abs(N-ans2))
        
def isPrime(nums):
    i = 2
    while i*i <= nums:
        if nums % i == 0:
            return False
        i += 1 
    return True

#Complexity:
#Time: O(n*sqrt(n))
#Space: O(1)

#Test Cases:
#74, 4585, 10236

print(NthTer(74))
print(NthTer(4585))
print(NthTer(10236))

#Link: https://practice.geeksforgeeks.org/problems/help-ishaan5837/1