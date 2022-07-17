def numberOfPairs(nums):
    dic = {}
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
    count1 = 0
    count2 = 0
    for i, j in dic.items():
        count1 = count1 + j//2
        count2 = count2 + j%2
    return [count1, count2]

#Complexity:
#Time: O(n+k)
#k is the legth of dictionary
#n is the length of nums

#Space: O(k)

print(numberOfPairs([1,3,2,1,3,2,2]))
print(numberOfPairs([1,1]))
print(numberOfPairs([0]))