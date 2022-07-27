def divisorGame(A, B, C):
    gcd = GCD(B, C)
    lcm = (B*C)//gcd
    count = (A)//lcm
    return count

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)