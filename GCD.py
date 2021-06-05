import math
def gcd(a,b):
    if(a<0):
        a=abs(a)
    elif(b<0):
        b=abs(b)
    if(b==0):
        return a
    else:
        return gcd(b,a%b)
try:
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
except:
    print("Number(s) should be integer only..")
    exit(0)
print(gcd(a,b))