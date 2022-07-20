def dNums(A, B):
    d = {}
    ans = []
    for i in range(B):
        d[A[i]] = d.get(A[i], 0) + 1 
    ans.append(len(d))
    i = 0
    for j in range(B, len(A)):
        d[A[j]] = d.get(A[j], 0) + 1
        d[A[i]] = d.get(A[i], 0) - 1
        if d[A[i]] == 0:
            del d[A[i]]
        i += 1
        ans.append(len(d))
    return ans

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1, 2, 1, 3, 4, 3], 3
#[1, 1, 2, 2], 1

print(dNums([1, 1, 2, 2], 1))
print(dNums([1, 2, 1, 3, 4, 3], 3))