def moveZeroesToTheEnd(nums):
    i=0
    k=0
    while(i<len(nums)):
        if(nums[i]!=0):
            nums[i], nums[k]= nums[k], nums[i]
            k+=1
        i+=1
    return nums
'''
Approach: k pointer will always point to a zero value and when i pointer points to non zero value then we swap both the values.

Complexity: Time-O(N), Space- O(1)

Test Cases:
nums = [0,1,0,3,12]
nums = [0]
'''
nums = [0,1,0,3,12]
print(moveZeroesToTheEnd(nums))
       