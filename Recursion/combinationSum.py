def combinationSum(candidates, target):
        return combination(candidates, 0, len(candidates), target, [], [])
    
def combination(arr, i, n, target, out, output):
    if i == n:
        if target == 0:
            output.append(out)
            out = []
        return
    if target >= arr[i]:
        combination(arr, i, n, target-arr[i], out+[arr[i]], output)
    
    combination(arr, i+1, n, target, out, output)
    
    return output
        
#Complexity:
#Time: O(2^n*target*n)
#Space: O(n*target)

#Test Cases:
#[2,3,6,7], 7
#[2,3,5], 8
#[2], 1

print(combinationSum([2,3,6,7], 7))
print(combinationSum([2,3,5], 8))
print(combinationSum([2], 1))
print(combinationSum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30], 500))

#Link: https://leetcode.com/problems/combination-sum/

#[1,2,3,4,5]