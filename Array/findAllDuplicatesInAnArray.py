def findDuplicates(nums):
    duplicates = []
    i = 0
    while(i < len(nums)):
        j = nums[i]
        if(nums[i] != nums[j-1]):
            nums[i], nums[j-1] = nums[j-1], nums[i]
        else:
            i += 1
    for index in range(len(nums)):
        if(nums[index] != index+1):
            duplicates.append(nums[index])
    return duplicates

#Complexity:
#Time: O(n)
#Space: O(1) #Not considering the output list

#Test Cases:
#[4,3,2,7,8,2,3,1], [1,1,2], [1]

print(findDuplicates([4,3,2,7,8,2,3,1]))
print(findDuplicates([1,1,2]))
print(findDuplicates([1]))

#Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/