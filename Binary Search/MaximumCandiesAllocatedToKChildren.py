from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l = 1
        r = k*max(candies)
        max_num_of_candies = 0

        while l <= r:
            mid = l+(r-l)//2
            children_received_candies = self.count_children_receiving(candies, mid)
            if children_received_candies >= k:
                l = mid + 1
                max_num_of_candies = max(max_num_of_candies, mid)
            else:
                r = mid - 1
        return max_num_of_candies

    def count_children_receiving(self, candies, target_candies):
        children_count = 0
        for candy in candies:
            children_count += int(candy//target_candies)
        return children_count

#Complexity:
#Time: O(n log n)
#Space: O(1)

#Test Cases:
#[5,8,6], 3
#[1,2,6,8,6,7,3,5,2,5], 3

sol = Solution()

print(sol.maximumCandies([5,8,6], 3))
print(sol.maximumCandies([1,2,6,8,6,7,3,5,2,5], 3))

#Link: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/?envType=daily-question&envId=2025-03-14
