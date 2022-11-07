def maximumSubarraySum(nums, k):
    sumi = 0
    maxSum = 0
    freqDict = {}
    
    for i in range(k):
        sumi += nums[i]
        freqDict[nums[i]] = freqDict.get(nums[i], 0) + 1 
        
        
    if len(freqDict) == k:  
        maxSum = sumi
        
    for i in range(k, len(nums)):
        sumi -= nums[i-k]
        
        freqDict[nums[i-k]] -= 1
        
        if freqDict[nums[i-k]] == 0:
            del freqDict[nums[i-k]]
                
        sumi += nums[i]
        freqDict[nums[i]] = freqDict.get(nums[i], 0) + 1 
        
        if len(freqDict) == k:
            maxSum = max(maxSum, sumi)
        
    return maxSum

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1,5,4,2,9,9,9], 3
#[4,4,4], 3

print(maximumSubarraySum([1,5,4,2,9,9,9], 3))
print(maximumSubarraySum([4,4,4], 3))

#Link: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/