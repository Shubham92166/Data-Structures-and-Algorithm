def solve(A, B, C):
    numerator = 1
    denominator = 1
    B = min(B, A-B)
    for i in range(B):
        numerator = (numerator*(A-i)) % C 
        denominator = (denominator*(i+1)) % C 
    return (numerator % C) * (binomialExp(denominator, C-2, C) % C) % C



def binomialExp(A, B, C):
    if B < 0:
        return A
    if B == 0:
        return 1 if A != 0 else 0
    else:
        if B % 2 == 0:
            return binomialExp((A*A)%C, B//2, C) % C
        else:
            return (A * binomialExp((A*A)%C, (B-1)//2, C) % C )%C

#Complexity:
#Time: O(B+(A-B))
#Space: O(1)

#Test Cases:
#5, 2, 13
#6, 2, 13
#105450, 3, 44

print(solve(5,2,13))
print(solve(6,2,13))
print(solve(105450,3,44))
