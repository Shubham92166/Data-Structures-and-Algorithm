def relativeSortArray(A, B):
    dic1 = {}
    dic2 = {}
    ans = []
    for i in A:
        dic1[i] = dic1.get(i, 0)+1
    for i in B:
        dic2[i] = dic2.get(i, 0)+1
    for i in B:
        val = dic1.get(i, -1)
        if val != -1:
            ans.extend([i]*val)
    for i in sorted(A):
        if i not in dic2:
            ans.append(i)
    return ans

#Complexity:
#Time: O(nlogn)
#Space: O(n+m) #n is the length of A and m is the length of B  

#Test Cases:
#[2, 1, 2, 3, 4, 5, 4, 5, 4, 2], [3, 5, 4, 2]
#[1, 2, 3, 4, 5], [5, 4, 2]
#[5, 17, 100, 11], [1, 100]
#[2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]
#[28,6,22,8,44,17], [22,28,8,6]

print(relativeSortArray([2, 1, 2, 3, 4, 5, 4, 5, 4, 2], [5, 4, 2]))
print(relativeSortArray([1, 2, 3, 4, 5], [5, 4, 2]))
print(relativeSortArray([5, 17, 100, 11], [1, 100]))
print(relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
print(relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))

#Link: https://leetcode.com/problems/relative-sort-array/