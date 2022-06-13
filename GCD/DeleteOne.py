import math
def deleteOne(A):
    gcd = 0
    n = len(A)
    pre = [0]*(n)
    post = [0]*(n)
    
    pre[0] = A[0]
    for i in range(1, n):
        pre[i] = Gcd(pre[i-1], A[i])
    
    post[-1] = A[-1]
    for i in range(n-2, -1, -1):
        post[i] = Gcd(post[i+1], A[i])
    
    maxGcd = 0
    for i in range(n):
        if i == 0:
            maxGcd = max(maxGcd, post[i+1])
        elif i == n-1:
            maxGcd = max(maxGcd, pre[i-1])
        else:
            gcd = Gcd(pre[i-1], post[i+1]) 
            maxGcd = max(gcd, maxGcd)
    return maxGcd

def Gcd(a, b):
    if a == 0 and b == 0:
        return math.inf
    elif a == 0:
        return b
    elif b == 0:
        return a
    return Gcd(b, a%b)

#Complexity:
#Time: O(nlog(max(A)))
#Space: O(nlog(max(A)))

#Test Cases:
#[12, 15, 18], [5, 15, 30]

print(deleteOne([5, 15, 30]))
print(deleteOne([12, 15, 18]))
