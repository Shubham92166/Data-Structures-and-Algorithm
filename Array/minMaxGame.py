def minMaxGame(nums):
    while(len(nums) > 1):
        n = len(nums)
        half = n//2
        newNums = [0]*half
        for i in range(half):
            if i%2 == 0:
                newNums[i] = min(nums[2 * i], nums[2 * i + 1])
            else:
                newNums[i] = max(nums[2 * i], nums[2 * i + 1])
        nums = newNums
    return nums[0]

#Complexity:
#Time: O(nlogn)
#Space: O(n)

#Test Cases:
#[1,3,5,2,4,8,2,2], [3]

print(minMaxGame([1,3,5,2,4,8,2,2]))
print(minMaxGame([3]))