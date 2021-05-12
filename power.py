def power(base, exp):
    assert exp>=0 and int(exp)==exp,"Exponent cannot be a float or negative value "
    if(exp==0):
        return 1
    elif(exp==1):
        return base
    else:
        return base*power(base,exp-1)
base, exp=map(int,input("Enter base and exponent:").split())
print(power(base,exp))
