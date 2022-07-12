def nthMagicalNumber(n, a, b):
    l = min(a, b)
    r = n*l
    lcm = (a*b)//GCD(a, b)
    while(l <= r):
        mid = l+(r-l)//2
        if (mid//a + mid//b - mid//lcm) < n:
            l = mid+1
        else:
            r = mid-1
    return l % ((10**9)+7)
    
def GCD(a, b):
    while(b > 0):
        a, b = b, a % b
    return a


#Complexity:
#Time: O(nlog(min(a, b)))
#Space: O(1)

#Test Cases:
#n = 1, a = 2, b = 3
#n = 4, a = 2, b = 3

print(nthMagicalNumber(1, 2, 3))
print(nthMagicalNumber(4, 2, 3))