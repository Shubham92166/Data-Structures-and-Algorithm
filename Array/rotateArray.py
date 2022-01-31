#Approach-1: Using Block Swap Algorithm

def rotate(nums, k):
        n=len(nums)
        if(k>n):
            k%=n
        rotateArray(nums, 0, n-k-1)
        rotateArray(nums, n-k, n-1)
        rotateArray(nums, 0, n-1)
        return nums
        
def rotateArray(nums, l, r):
    while(l<=r):
        nums[l], nums[r]=nums[r], nums[l]
        l+=1
        r-=1

#Test Cases: 
#[1,2,3,4,5,6], 11
#[1,2,3,4,5,6,7], 3
#[-1,-100,3,99], 2

#Complexity:
#Time: O(N)
#Space: O(1)

print(rotate([-1,-100,3,99], 2))
print(rotate([1,2,3,4,5,6], 11))
print(rotate([1,2,3,4,5,6,7], 3))

