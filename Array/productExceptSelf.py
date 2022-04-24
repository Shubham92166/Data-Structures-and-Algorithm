def productExceptSelf(nums):
    PM = [1]*len(nums)
    SM = [1]*len(nums)
    PM[0] = nums[0]
    n = len(nums)
    res = [1]*len(nums)
    for i in range(1, len(nums)):
            PM[i] = nums[i]*PM[i-1]
    SM[n-1] = nums[n-1]
    for i in range(n-2, -1, -1):
            SM[i] = nums[i]*SM[i+1]
    for i in range(len(nums)):
        if i == 0:
            res[i] = SM[i+1]
        elif i == n-1:
            res[i] = PM[i-1]
        else:
            res[i] = SM[i+1]*PM[i-1]
    return res

#Test Cases:
#[1,2,3,4], [-1,1,0,-3,3]

#Complexity:
#Time: O(N)
#Space: O(N)

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))
    