def subsetsWithDup(nums):
        res = []
        all_subsets = set()
        return helper(nums, 0, res, all_subsets, [])
           
def helper(nums, i, res, all_subsets, subset):
    if i == len(nums):
        subset.sort()
        subsetTuple = tuple(subset)
        if subsetTuple not in all_subsets:
            res.append(subset)
            all_subsets.add(subsetTuple)
        return 
    
    helper(nums, i+1, res, all_subsets, subset + [nums[i]])
    helper(nums, i+1, res, all_subsets, subset)
    return res

#Complexity:
#Time: O((n log n)*2^n)
#Space: O(n)

#Test Cases:
#[1,2,2], [0], [1,1,1,2,2,6,4,2,7]

print(subsetsWithDup([1,2,2]))
print(subsetsWithDup([0]))
print(subsetsWithDup([1,1,1,2,2,6,4,2,7]))

#Link: https://leetcode.com/problems/subsets-ii/