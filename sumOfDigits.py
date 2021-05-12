def sumOfDigits(n):
    assert n>=0 and int(n)==n," Number cannot be negative"
    if(n==0):
        return 0
    else:
        return int(n%10)+sumOfDigits(int(n/10))
n=int(input("Enter any number:"))
print(sumOfDigits(n))
