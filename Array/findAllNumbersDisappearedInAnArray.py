def findDisappearedNumbers(nums):
    i = 0
    while(i < len(nums)):
        j = nums[i]
        if(nums[i] != nums[j-1]):
            nums[i], nums[j-1] = nums[j-1], nums[i]
        else:
            i += 1
    
    disappeared = []
    
    for i in range(len(nums)):
        if nums[i]-1 != i:
            disappeared.append(i+1)
    
    return disappeared

#Complexity:
#Time: O(n)
#Space: O(1) #Not considering the output list

#Test Cases:
#[4,3,2,7,8,2,3,1], [1, 1]

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1, 1]))

#Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
