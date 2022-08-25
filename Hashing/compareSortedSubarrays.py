import random

def solve(A, B):
    ans = []

    hashes = hashFunction(A)
    prefixSum = [0]*len(A)
    prefixSum[0] = hashes[A[0]]

    for i in range(1, len(A)):
        prefixSum[i] = prefixSum[i-1]+hashes[A[i]]
    
    for q in B:
        if q[0] > 0:
            val1 = prefixSum[q[1]] - prefixSum[q[0]-1]
        else:
            val1 = prefixSum[q[1]]
        if q[2] > 0:
            val2 = prefixSum[q[3]] - prefixSum[q[2]-1]
        else:
            val2 = prefixSum[q[3]] 
        
        if abs(val1) == abs(val2):
            ans.append(1)
        else:
            ans.append(0)
    return ans

def hashFunction(A):
    hashes = {}
    for i in A:
        if hashes.get(i, -1) == -1:
            hashes[i] = random.randint(0, 1000000007)*i*100000
    return hashes

#Complexity:
#Time: O(n+m)
#Space: O(n)
#where n is the length of A and m is the length of B

#Test Cases:
#[1, 7, 11, 8, 11, 7, 1], [[0, 2, 4, 6]]
#[1, 3, 2], [[0, 1, 1, 2]] 

print(solve([1, 7, 11, 8, 11, 7, 1], [[0, 2, 4, 6]]))
print(solve([1, 3, 2], [[0, 1, 1, 2]]))