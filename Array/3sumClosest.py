import sys
def sumClosest(nums, target):
    closest = sys.maxsize
    nums.sort()
    for i in range(len(nums)-2):
        l = i+1
        r = len(nums)-1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if abs(target-sum) < abs(target - closest):
                closest = sum
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            elif sum == target:
                return target
    return closest

#Complexity:
#Time: O(n^2)
#Space: O(1)

#Test Cases:
#[-1, 2, 1, -4], 1
#[1, 2, 3], 6
#[0,0,0], 0

print(sumClosest([0,0,0], 0))
print(sumClosest([-1, 2, 1, -4], 1))
print(sumClosest([1, 2, 3], 6))