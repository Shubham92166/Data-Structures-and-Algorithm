def reverse(n):
    if(n%2==0):
        return n
    else:
        return int(n/10)*10+reverse(int(n%10))
    
print(reverse(20))