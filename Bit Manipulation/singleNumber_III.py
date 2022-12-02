def singleNumber(A):
    res = [0]*2
    xor = 0
    for i in range(len(A)):
        xor = xor ^ A[i]
    lastSetBit = xor & (-xor)
    for i in A:
        if (lastSetBit & i): 
            res[0] = res[0] ^ i 
        else:
            res[1] = res[1] ^ i
    return res

#Complexity:
#Time: O(n)
#Space: (1)

#Test Cases:
#[1,2,1,3,2,5], [-1,0], [0,1]

print(singleNumber([1,2,1,3,2,5]))
print(singleNumber([-1,0]))
print(singleNumber([0,1]))

#Link: https://leetcode.com/problems/single-number-iii/

