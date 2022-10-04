def shipWithinDays(weights, days):
    totalWeight = sum(weights)
    maxWeight = max(weights)
    
    l = maxWeight
    r = totalWeight
    
    ans = 10000000
    
    while l <= r :
        mid = l + (r-l)//2
        daysRequired = helper(weights, mid)
        if daysRequired > days:
            l = mid+1
        else:
            r = mid-1
            ans = min(ans, mid)
            
    return ans

def helper(weights, target):
    count = 1
    sum = weights[0]
    for i in range(1, len(weights)):
        if sum + weights[i] > target:
            sum = 0
            count += 1   
        sum += weights[i]
    return count

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1,2,3,4,5,6,7,8,9,10], 5
#[3,2,2,4,1,4], 3
#[1,2,3,1,1], 4
#[5,8,9,10,56,74,5], 6
#[5,8,9,10,56,74,5], 5
#[5,8,9,10,56,74,5], 3

print(shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
print(shipWithinDays([3,2,2,4,1,4], 3))
print(shipWithinDays([1,2,3,1,1], 4))
print(shipWithinDays([5,8,9,10,56,74,5], 6))
print(shipWithinDays([5,8,9,10,56,74,5], 5))
print(shipWithinDays([5,8,9,10,56,74,5], 3))

#Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/