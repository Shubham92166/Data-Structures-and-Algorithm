#Approach: 
#We are using two pointers approach here. Here, all the positive elements should come at even indexs and negative elements should come 
#at odd indexes. So we keep two pointers, one at even index(0) and another at odd index(1). Based on the condition of odd and even we 
#put elements in the answer array and increment pointers by two.
 
def rearrangeArray(nums):
    i = 0
    j = 1
    
    ans = [0]*len(nums)
    for num in nums:
        if num > 0:
            ans[i] = num
            i += 2
        else:
            ans[j] = num
            j += 2
    
    return ans

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[3,1,-2,-5,2,-4], [-1,1]

print(rearrangeArray([3,1,-2,-5,2,-4]))
print(rearrangeArray([-1,1]))

#Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/