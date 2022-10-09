def findArray(pref):
    pre = [0]*len(pref)
    pre[0] = pref[0]
    
    for i in range(1, len(pref)):
        pre[i] = pref[i] ^ pref[i-1]
    return pre

#Complexity:
#Time: O(n)
#Space: O(n)
#where n is the size of the array

#Test Cases:
#[5,2,0,3,1], [13]

print(findArray([5,2,0,3,1]))
print(findArray([13]))

#Link: https://leetcode.com/problems/find-the-original-array-of-prefix-xor/