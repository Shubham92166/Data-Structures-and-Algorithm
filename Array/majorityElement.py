#Method1: Using Hashmap(brute force)

def majorityElement1(nums):
    dic={}
    for i in range(len(nums)):
        dic[nums[i]] = dic.get(nums[i], 0) + 1
    
    required_freq = len(nums)//2

    for key, val in dic.items():
        if val > required_freq:
            return key

    return -1 

#Complexity:
#Time: O(n)
#Space: O(n)

#Method2-Using Boyer's Moore Voting Algorithm

"""
Approach:
1. Assume that first element of the array is the majority element and its frequency is 1
2. Now traverse from second element array[1] to last element of the array.
3. If the cur_element is equal to majority element then increment the frequency
4. If cur_element is not equal to majority element then decrement the frequency.
5. If the frequency is equal to zero means there is no majority element and cur_element will become the majority element and its 
frequency will become 1 now
6. At the end, there could be two scenarios:
A) There exist a majority element
B) There is no majority element
7. Now, to check step 6, run a loop again on the array and check whether the majority element returned from the algorithm is correct
or not.
8. If it is correct then return the majority element else return -1 as there is no majority element
"""

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