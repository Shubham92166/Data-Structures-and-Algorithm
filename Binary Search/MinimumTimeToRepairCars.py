import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_time = math.inf

        l = 1
        r = min(ranks)*cars**2

        while l <= r:
            mid = l+(r-l)//2

            number_of_repaired_cars = self.count_repaired_cars_in_given_time(ranks, mid)
            if number_of_repaired_cars >= cars:
                min_time = min(min_time, mid)
                r = mid - 1
            else:
                l = mid + 1
        return  min_time

    def count_repaired_cars_in_given_time(self, ranks, target_time):
        count_cars = 0
        for rank in ranks:
            count_cars += int((target_time//rank)**0.5)
        
        return count_cars

#Complexity:
#Time: O(n log n)
#Space: O(1)

#Test Cases:
#[4,2,3,1], 10
#[5,1,8], 6

sol = Solution()

print(sol.repairCars([4,2,3,1], 10))
print(sol.repairCars([5,1,8], 6))

#Link: https://leetcode.com/problems/minimum-time-to-repair-cars/description/?envType=daily-question&envId=2025-03-16