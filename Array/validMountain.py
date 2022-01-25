def validMountain(nums):
    
    #if the length is less than 3 then we need to return False

    #Test Case: [1], [1,2], [2,1], [0,0]
    
    if(len(nums)<3):
        return False
    
    #we take two pointers from starting and end of the list

    i=0
    j=len(nums)-1

    #with the help of the starting pointer, iterate until element at index i+1> element at index i. 
    #However, if the pointer has reached to the end that means there is no decreasing element and pointer has reached to the end
    # If so, we will return False as we do not find any decreasing element
    #Else we will keep iterating the list

    #Valid Test Case: [1,2,4,5,3,2,1,0]

    while(nums[i+1]>nums[i]):

        #Test Case: [1,2,3,4], [1,2,8,40,45,74]

        if(i+1==len(nums)-1):
            return False
        i+=1
    #with the help of the end pointer, iterate until element at index j-1> element at index j. 
    #However, if the pointer has reached to the begining that means there is no increasing element and pointer has reached 
    #to the begining
    # If so, we will return False as we do not find any increasing element
    #Else we will keep iterating the list    

    while(nums[j-1]>nums[j]):
        if(j==1):

            #Test Case: [7,6,5,4,3,2,1]

            return False
        j-=1

    #If there is any duplicate element then i and j wil not be equal and we need to return False. Therefore, we check whether
    #i is equal to j or not. If they are not, that means there was any duplicate element or it found some increasing and decreasing
    #pattern in the same part of the array while traversing

    if(i==j):
        return True
    
    #Test Case: [1,2,3,3,4,4], [1,4,5,6,3,3,4,5]

    return False

print(validMountain([1,2,3,3,4,4]))
print(validMountain([1,4,5,6,3,3,4,5]))
print(validMountain([7,6,5,4,3,2,1]))
print(validMountain([1,2,8,40,45,74]))
print(validMountain([1,2]))
print(validMountain([2,0,2]))
print(validMountain([1,2,4,5,3,2,1,0]))

