def removeDuplicates(nums):
    count=i=j=1
    while(i<len(nums)):
        if(nums[i]==nums[i-1]):
            count+=1 
        else:
            count = 1
        if(count<=2):
            nums[j] = nums[i]
            j+=1
        i+=1
    return nums[:j]

#Test Cases: [1,1,1,2,2,3], [0,0,1,1,1,1,2,3,3], [1,2,2,3,3,3,4,4,4,4]

#Complexity:
#Time: O(N)
#Space: O(1)

print(removeDuplicates([0,0,1,1,1,1,2,3,3]))
print(removeDuplicates([1,2,2,3,3,3,4,4,4,4]))
print(removeDuplicates([1,1,1,2,2,3]))     