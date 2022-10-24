def fourSum(nums, target):
    if len(nums) < 4:
         return []
    nums.sort()
    ans = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)-2):
            l = j+1
            r = len(nums)-1
            while l < r:
                pairs = (nums[i], nums[j], nums[l], nums[r])
                sumOfPairs = sum(pairs)
                if sumOfPairs < target:
                    l += 1
                elif sumOfPairs > target:
                    r -= 1
                else:
                    ans.add(pairs)
                    l += 1
                    r -= 1
    return list(ans)

#Complexity:
#Time: O(n^3)
#Space: O(1)

#Test Cases:
#[1,0,-1,0,-2,2], 0
#[2,2,2,2,2], 8

print(fourSum([2,2,2,2,2], 8))
print(fourSum([1,0,-1,0,-2,2], 0))