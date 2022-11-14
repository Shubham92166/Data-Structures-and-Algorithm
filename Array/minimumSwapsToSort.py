def minSwaps(nums):
    l = []
    n = len(nums)
    for i in range(n):
        l.append((nums[i], i))

    l = sorted(l, key = lambda x: x[0])

    swaps = 0
    index = 0

    while index < n:
        if index == l[index][1]:
            index += 1
        else:
            temp = l[index][1]
            l[index], l[temp] = l[temp], l[index]
            swaps += 1
        
    return swaps

#Complexity:
#Time: O(nlog n)
#Space: O(n)

#Test Cases:
#[2, 8, 5, 4], [10, 19, 6, 3, 5]

print(minSwaps([2, 8, 5, 4]))
print(minSwaps([10, 19, 6, 3, 5]))

#Link: https://practice.geeksforgeeks.org/problems/minimum-swaps/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article