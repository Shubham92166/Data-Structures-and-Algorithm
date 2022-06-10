def pairSumDivisibleByM(nums, k):
    if len(nums) == 1:
        return 0
    dic1 = {}
    modK = [((nums[i]) % k + k) % k  for i in range(len(nums))]
    for i in range(len(modK)):
        dic1[modK[i]] = dic1.get(modK[i], 0) + 1
    dic = {}
    for i in range(k):
        if i in dic1 and i in dic:
            dic[i] += 1
        elif i in dic1 and i not in dic:
            dic[i] = dic1[i]
        else:
            dic[i] = 0 
    ans = 0
    if 0 in dic and dic[0] > 0:
        value = dic[0]
        ans += (value*(value-1))//2
    for i in range(1, k//2):
        ans += (dic[i] * dic[k-i])
    
    if k%2 == 0:
        n = (dic[k//2])
        ans += ((n*(n-1))//2) 
    else:
        ans += (dic[k//2]*dic[(k//2)+1])
    return ans % (pow(10, 9)+7)

#Complexity:
#Time: O(n+k)
#Space: O(n)

#Test Case:
#[1, 2, 3, 4, 5], 2
#[5, 17, 100, 11], 28

print(pairSumDivisibleByM([5, 17, 100, 11], 28))
print(pairSumDivisibleByM([1, 2, 3, 4, 5], 2))

