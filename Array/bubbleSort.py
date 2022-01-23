def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if(nums[j+1]<nums[j]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

#---------Optimized code-----------#
#This will reduce the no. of iteration if the array is sorted in iteration<<n
def optimizedBubbleSort(nums):
    for i in range(len(nums)):
        swapped=False
        for j in range(len(nums)-i-1):
            swapped=True
            if(nums[j+1]<nums[j]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
        if(not swapped):
            break
    return nums

nums=[4,3,7,1,5]
print(bubbleSort(nums))
print(optimizedBubbleSort(nums))

