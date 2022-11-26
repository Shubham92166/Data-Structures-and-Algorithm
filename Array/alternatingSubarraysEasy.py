'''
You are given an integer array A of length N comprising of 0's & 1's, and an integer B. You have to tell all the indices of array A 
that can act as a center of 2 * B + 1 length 0-1 alternating subarray. A 0-1 alternating array is an array containing only 0's & 1's, 
and having no adjacent 0's or 1's. For e.g. arrays [0, 1, 0, 1], [1, 0] and [1] are 0-1 alternating, while [1, 1] and [0, 1, 0, 0, 1] 
are not.

Problem Constraints
1 <= N <= 103
A[i] equals to 0 or 1.
0 <= B <= (N - 1) / 2
'''

def solve(A, B):
    lengthOfASubarray = 2*B+1
    noOfSubarrays = len(A)-lengthOfASubarray+1
    ans = []

    for i in range(noOfSubarrays):
        flag = False
        prev = -1

        for j in range(i, i+lengthOfASubarray):
            if A[j] == prev:
                flag = True
                break
            
            prev = A[j]
        
        if not flag:
            ans.append(i+B)
    
    return ans

#Complexity:
#Time: O(B(N-B)) ==> O(NB+B^2)
#Space: O(1)

#Test Cases:
#[1, 0, 1, 0, 1], 1 
#[0, 0, 0, 1, 1, 0, 1], 0

print(solve([1, 0, 1, 0, 1], 1))
print(solve([0, 0, 0, 1, 1, 0, 1], 0)) 