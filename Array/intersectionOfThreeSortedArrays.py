#Method1:
def commonElements1(A, B, C, n1, n2, n3):
    i = 0
    j = 0
    k = 0
    res = set()
    while(i < n1 and j < n2 and k < n3):
        if A[i] < C[k] and B[j] < C[k]:
            i += 1 
            j += 1
        elif A[i] < B[j] and C[k] < B[j]:
            i += 1
            k += 1
        elif B[j] < A[i] and C[k] < A[i]:
            j += 1
            k += 1
        elif A[i] == B[j] and B[j] == C[k]:
            res.add(A[i])
            i += 1
            j += 1
            k += 1
        elif A[i] == B[j] and C[k] < B[j]:
            k += 1
        elif A[i] == C[k] and C[k] > B[j]:
            j += 1
        elif B[j] == C[k] and C[k] > A[i]:
            i += 1
    return sorted(list(res))

#Complexity:
#Time: O((n1+n2+n3)log(n1+n2+n3))
#Space: O(n1+n2+n3) 

#Method2:
def commonElements2(A, B, C, n1, n2, n3):
    i = 0
    j = 0
    k = 0
    res = []
    while(i < n1 and j < n2 and k < n3):
        if A[i] == C[k] and B[j] == C[k]:
            res.append(A[i])
            i += 1 
            j += 1
            k += 1
            
        elif A[i] < B[j]:
            i += 1
        elif B[j] < C[k]:
            j += 1
        else:
            k += 1
        if i > 0 and i < n1:
            x = A[i-1]
            while(i > 0 and i < n1 and x == A[i]):
                i += 1
        if j > 0 and j < n2:
            y = B[j-1]
            while(j > 0 and j < n2 and y == B[j]):
                j += 1
        if k > 0 and k < n3:
            z = C[k-1]
            while(k > 0 and k < n3 and z == C[k]):
                k += 1
    return res

#Complexity:
#Time: O((n1+n2+n3))
#Space: O(1)

#Test Cases:
#A = [1, 5, 10, 20, 40, 80]
#B = [6, 7, 20, 80, 100]
#C = [3, 4, 15, 20, 30, 70, 80, 120]




print(commonElements1([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120], len([1, 5, 10, 20, 40, 80]), len([6, 7, 20, 80, 100]), len([3, 4, 15, 20, 30, 70, 80, 120])))
print(commonElements2([1, 5, 10, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120], len([1, 5, 10, 20, 40, 80]), len([6, 7, 20, 80, 100]), len([3, 4, 15, 20, 30, 70, 80, 120])))
