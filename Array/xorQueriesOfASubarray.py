def xorQueries(arr, queries):
    ans = []
    N = len(arr)
    
    xorArray = [0]*N
    
    xorArray[0] = arr[0]
    
    for i in range(1, N):
        xorArray[i] = arr[i]^xorArray[i-1]
        
    for q in queries:
        start = q[0]
        end = q[1]
        if start == 0:
            ans.append(xorArray[end])
        else:
            xor = xorArray[end] ^ xorArray[start-1]
            ans.append(xor)
    
    return ans

#Complexity:
#Time: O(n + Q)
#Space: O(n)
#Where n is the length of the array and Q is the no. of queries

#Test Cases:
#[1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]
#[4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]

print(xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))
print(xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]))

#Link: https://leetcode.com/problems/xor-queries-of-a-subarray/