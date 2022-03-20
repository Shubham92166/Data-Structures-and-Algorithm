#------Solution in O(N) using two pointers approach----------#
def twoSum(nums, target):
        l, r =0, len(nums)-1
        while(l<=r):
            if(nums[l]+nums[r]>target):
                r-=1
            elif(nums[l]+nums[r]<target):
                l+=1
            elif(nums[l]+nums[r]==target):
                break
        return [l+1, r+1]
 

 #--------Solution in Nlog(N) using Binary Search-----------#

#Searching the target-current element using Binary Search
def findElementInArray(nums,target):
    l=0
    r=len(nums)-1
    while(l<=r):
        mid=(l+r)//2
        if(nums[mid]==target):
            return mid
        elif(nums[mid]<target):
            l=mid+1
        else:
            r=mid-1
    return -1

def twoSum(nums, target):
    for i in range(len(nums)):
            findElement=target-nums[i]
            indexOfOtherElement=findElementInArray(nums,findElement)
            if(indexOfOtherElement!=-1 and indexOfOtherElement!=i): #Since we cannot use same element twice
                return [i+1, indexOfOtherElement+1] #Array is 1-indexed

'''
TestCases:
nums= [2,7,11,15], target = 9
nums= [2,3,4], target = 6
nums= [-1,0], target = -1
'''



