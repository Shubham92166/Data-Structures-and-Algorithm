def averageValue(nums):
    divisibleBy3 = []
    for num in nums:
        if num % 3 == 0 and num % 2 == 0:
            divisibleBy3.append(num)
    
    if divisibleBy3:
        return sum(divisibleBy3)//len(divisibleBy3)
    else:
        return 0

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1,3,6,10,12,15], [1,2,4,7,10]

print(averageValue([1,3,6,10,12,15]))
print(averageValue([1,2,4,7,10]))

#Link: https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/