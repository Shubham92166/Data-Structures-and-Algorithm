def minOperations(nums, numsDivide):
    dic = {}
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
    count = 0
    dic = dict(sorted(dic.items(), key = lambda item: item[0]))
    for key, value in dic.items():
        res = checkDivisibility(key, numsDivide)
        if res == False:
            count += value
        else:
            return count
    return -1  

def checkDivisibility(k, nums):
    for i in nums:
        if i % k != 0:
            return False
    return True

#Complexity:
#Time: O(klogk + km) 

#k is the length of dictionary
#n is the length of nums
#m is the length of numsDivide

#Space: O(k) 

#Test Cases:
#[2,3,2,4,3], [9,6,9,3,15]
#[4,3,6], [8,2,6,10]

print(minOperations([4,3,6], [8,2,6,10]))
print(minOperations([2,3,2,4,3], [9,6,9,3,15]))


