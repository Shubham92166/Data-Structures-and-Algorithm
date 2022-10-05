import math
def minEatingSpeed(piles, h):
    l = 1
    r = max(piles)
    ans = math.inf
    while l <= r:
        mid = l +(r-l)//2
        hRequired = calculateH(piles, mid)
        if hRequired > h:
            l = mid+1
        else:
            r = mid-1
            ans = min(ans, mid)
    return ans

def calculateH(piles, target):
    totalH = 0
    for i in range(len(piles)):
        if piles[i] <= target:
            totalH += 1
        else:
            totalH += math.ceil(piles[i]/target)
    return totalH

#Complexity:
#Time: O(n logn)
#Space: O(1)

#Test Cases:
#[3,6,7,11], 8
#[30,11,23,4,20], 5
#[30,11,23,4,20], 6

print(minEatingSpeed([3,6,7,11], 8))
print(minEatingSpeed([30,11,23,4,20], 5))
print(minEatingSpeed([30,11,23,4,20], 6))

#Link: https://leetcode.com/problems/koko-eating-bananas/