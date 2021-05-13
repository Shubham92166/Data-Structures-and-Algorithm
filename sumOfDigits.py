def sumOfDigits(n):
    assert n>0, "Number cannot be negative"
    if(n==0):
        return 0
    else:
        return int(n%10)+sumOfDigits(int(n/10))
try:
    n=int(input("Enter any number:"))
except:
    print("Number should be positive integer only...")
    exit(0)
print(sumOfDigits(n))
