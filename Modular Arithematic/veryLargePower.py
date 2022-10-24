import sys
sys.setrecursionlimit(10**6)
def solve(A, B):
    res = 0
    mod =  1000000007
    factOfB = fact(B, mod)
    x = factOfB % (mod-1)
    res = binexp(A, factOfB, mod) % mod
    return res

def binexp(n, p, m):
    if p == 0:
        return 1
    x = binexp(n, p//2, m)
    x = (x*x) % m
    if p % 2 == 0:
        return x
    else:
        return (x*n) % m

def fact(n, mod):
    fact = 1
    while n > 0:
        fact = (fact *n) % (mod-1) 
        n -= 1
    return fact

#Complexity:
#Time: O(B + log(1000000007))
#Space: O(log(1000000007))

#Test Cases:
#452211, 4554646
#45655455, 8566666

print(solve(452211, 4554646))
print(solve(45655455, 8566666))