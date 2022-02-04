def maxSubArrayWithSumZero(nums):    
    elements = {}
    sum = 0
    max_length = 0
    elements[0] = -1
    for i in range(len(nums)):
        sum+= nums[i]
        if sum in elements:
            max_length= max(max_length, i-elements[sum])
        else:
            elements[sum] = i
    return max_length

#Test Cases: [-1], [0], [-1, 1], [4,7,5,-3,3,4]

#Complexity: 
#Time: O(n)
#Space: O(n)


print(maxSubArrayWithSumZero([-1]))
print(maxSubArrayWithSumZero([-1,1]))
print(maxSubArrayWithSumZero([1,4,3,-3,5]))

