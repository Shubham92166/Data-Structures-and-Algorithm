def solve(A, B):
    pre = [0]*(A+2)
    for q in B:
        pre[q[0]] += q[2]
        pre[q[1]+1] -= q[2]
    for i in range(1, len(pre)):
        pre[i] = pre[i]+pre[i-1]
    return pre[1:-1]

#Complexity:
#Time: O(A+B)
#Space: O(A)

#Test Cases:
#5, [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

print(solve(5, [[1, 2, 10], [2, 3, 20], [2, 5, 25]]))
