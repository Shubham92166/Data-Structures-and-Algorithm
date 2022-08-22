class NumArray:
    def __init__(self, nums):
        self.nums = nums
        self.PS = [0] * len(nums)
        self.PS = self.prefixSum(nums)
        

    def sumRange(self, left, right):
        if left == 0:
            return self.PS[right] 
        else:
            return self.PS[right] - self.PS[left-1]
        
    def prefixSum(self, nums):
        self.PS[0] = nums[0]
        for i in range(1, len(nums)):
            self.PS[i] = self.PS[i-1] + nums[i]
        return self.PS

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#["NumArray", "sumRange", "sumRange", "sumRange"], [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

#Link: https://leetcode.com/problems/range-sum-query-immutable/