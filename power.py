try:
    def power(base, exp):
        if(exp<0):
            print("Exponent cannot be negative..")
            exit(0)
        if(exp==0):
            return 1
        elif(exp==1):
            return base
        else:
            return base*power(base,exp-1)

    base, exp=map(int,input("Enter base and exponent:").split())
except:
    print("Number(s) should be integer only..")
    exit(0)
print(power(base,exp))
