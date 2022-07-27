#Method1: Using Hashmap(brute force)

def majorityElement1(nums):
    dic={}
    for i in set(nums):
        dic[i]=nums.count(i)
    {k: v for k,v in sorted(dic.items(), key=lambda item: item[1])}
    value=max(dic.values())
    for i, j in dic.items():
        if(j==value):
            return i

#Complexity:
#Time: O(nlog n)
#Space: O(n)

#Method2-Using Boyer's Moore Voting Algorithm

def majorityElement2(A):
    majority = A[0]
    freq = 1
    for i in range(1, len(A)):
        if freq == 0:
            majority = A[i]
            freq = 1
        elif majority == A[i]:
            freq += 1
        elif A[i] != majority:
            freq -= 1
    return majority

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[3,2,3], [2,2,1,1,1,2,2], [6,5,5], [3,3,4]


#For method1:
#--------------#

print(majorityElement1([2,2,1,1,1,2,2]))
print(majorityElement1([3,2,3]))
print(majorityElement1([6,5,5]))
print(majorityElement1([3,3,4]))

#For method2:
#--------------#

print(majorityElement2([2,2,1,1,1,2,2]))
print(majorityElement2([3,2,3]))
print(majorityElement2([6,5,5]))
print(majorityElement2([3,3,4]))
#Link: https://leetcode.com/problems/majority-element/