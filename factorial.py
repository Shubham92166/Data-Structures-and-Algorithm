try:
    n=int(input("Enter any number:"))
    assert n>=0, "Number cannot be negative.."
    def factorial(n):
        if(n in [0,1]):
            return 1
        else:
            return n*factorial(n-1)
except:
    print("Number should be positive integer only..")
    exit(0)
print(factorial(n))
