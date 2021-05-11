n=int(input("Enter any number"))
def factorial(n):
    assert n>=0 and int(n)==n, "Number cannot be negative"
    if(n in [0,1]):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))
