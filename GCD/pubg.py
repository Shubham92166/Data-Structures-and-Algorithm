def pubg(A):
    gcd = 0
    for i in A:
        gcd = GCD(gcd, i)
    return gcd

def GCD(a, b):
    if a == 0:
        return b
    if b == 0:
        return a 
    return GCD(b, a%b)

#Complexity:
#Time: 
#Space: 

#Test Cases:
#[2, 3, 4], [6,4]

print(pubg([2, 3, 4]))
print(pubg([6,4]))
