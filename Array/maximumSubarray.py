import math

def maxSubArray(nums):    
    cur=0
    maxi = -math.inf
    for i in range(len(nums)):
        cur += nums[i]
        if(maxi < cur):
            maxi = cur
        if(cur < 0):
            cur = 0
    return maxi

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8]

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([1]))
print(maxSubArray([5,4,-1,7,8]))

#Link: https://leetcode.com/problems/maximum-subarray/
        