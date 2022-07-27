def cpFact(A, B):
    while(GCD(A, B)!= 1):
        A = A//GCD(A, B)
    return A

def GCD(self, a, b):
    if b == 0:
        return a
    return self.GCD(b, a%b)


