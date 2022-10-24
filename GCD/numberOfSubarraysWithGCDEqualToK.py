'''
Approach:

We can use two loops to get the subarray and while finding the subarrays we can compute the GCD. If the GCD of the subarray is equal to
the k then we increment the count variable. At the end, we return the count.
'''
import math

def subarrayGCD(nums, k):
    count = 0
    for i in range(0, len(nums)):
        GCD = 0
        for j in range(i, len(nums)):
            GCD = math.gcd(GCD, nums[j])
            if GCD == k:
                count += 1
    return count

#Complexity:
#Time: O(n^2 log(max(nums)))
#Space: O(1)

#Test Cases:
#[9,3,1,2,6,3], 3
#[4], 7

print(subarrayGCD([9,3,1,2,6,3], 3))
print(subarrayGCD([4], 7))

#Link: https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/