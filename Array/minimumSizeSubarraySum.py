import math
def minSubArrayLen(target, nums):
    minLength = math.inf
    n = len(nums)
    
    curSum = 0
    start = 0
    end = 0
    
    while end < n:
        curSum += nums[end]
            
        while curSum >= target:
            minLength = min(minLength, end-start+1)
            curSum -= nums[start]
            start += 1
            
        end += 1
        
    if minLength == math.inf:
        return 0
    return minLength
        
#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#7, [2,3,1,2,4,3]
#4, [1,4,4]
#11, [1,1,1,1,1,1,1,1]

print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(4, [1,4,4]))
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))

#Link: https://leetcode.com/problems/minimum-size-subarray-sum/