import math
def mostFrequentEven(nums):
    dic = {}
    for i in (nums):
        if i % 2 == 0:
            dic[i] = dic.get(i, 0) + 1
    
    ans = math.inf

    if len(dic) == 0:
        return -1

    maxFreq = max(dic.values())
    
    for key, val in dic.items():
        if val == maxFreq:
            ans = min(ans, key)
    
    return ans

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[0,1,2,2,4,4,1], [4,4,4,9,2,4], [29,47,21,41,13,37,25,7]     

print(mostFrequentEven([0,1,2,2,4,4,1]))
print(mostFrequentEven([4,4,4,9,2,4]))
print(mostFrequentEven([29,47,21,41,13,37,25,7]))

#Link: https://leetcode.com/problems/most-frequent-even-element/