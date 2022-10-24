def sqrt(x):
    l, r = 0,  x
    while(l <= r):
        mid = (l+r)//2 
        square = mid*mid
        if(square == x):
            return mid
        elif(square > x):
            r = mid-1
        else:

            #if the x is not a perfect square then in that case we need to return the square root of a perfect sqaure where the 
            # number is less than x

            l = mid+1 
            res = mid
    return res

#Test Cases: 8, 4, 2, 0, 1, 120, 547, 624, 16

#Complexity:
#Time: O(log N)
#Space: O(1)

print(sqrt(547))
print(sqrt(120))
print(sqrt(624))
print(sqrt(0))
print(sqrt(1))
print(sqrt(4))
print(sqrt(16))

