#Method-1: Using extra space:

def pivotIndex1(nums):
    PS =[0]*len(nums)
    PS[0] = nums[0]
    n = len(nums)
    for i in range(1, len(nums)):
        PS[i] = PS[i-1] + nums[i]
    for i in range(len(nums)):
        if i == 0:
            left = 0
        else:
            left = PS[i-1]
        right = PS[n-1] - PS[i]
        if left == right:
            return i
    return -1

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1,7,3,6,5,6], [1,2,3], [2,1,-1]

#Run:

print(pivotIndex1([1,7,3,6,5,6]))
print(pivotIndex1( [1,2,3]))
print(pivotIndex1([2,1,-1]))

#Method-2: Without using extra space:

def pivotIndex2(nums):
    sumOfAll = sum(nums)
    
    leftSum = 0
    
    for i in range(len(nums)):
        leftSum += nums[i]
        if leftSum == sumOfAll:
            return i
        
        sumOfAll -= nums[i]
    
    return -1

#Complexity:
#Time: O(n)
#Space: O(1)

#Run:

print(pivotIndex2([1,7,3,6,5,6]))
print(pivotIndex2( [1,2,3]))
print(pivotIndex2([2,1,-1]))

#Link: https://leetcode.com/problems/find-pivot-index/