#Method 1:
def squareSumMethod1(c):
    a = 0
    while(a*a <= c):
        if binarySearch(0, c-a*a) == True:
            return True
        a += 1
    return False
    
def binarySearch(a, b):
    l = a
    r = b
    while(l <= r):
        mid = l+(r-l)//2
        square = mid*mid
        if square == b:
            return True
        elif square > b:
            r = mid-1
        else:
            l = mid+1
    return False

#Complexity:
#Time: O(sqrt(c)log(c))
#Space: O(1)
                
#Method 2:
def squareSumMethod2(c):
    i = 2
    while(i*i <= c):
        count = 0
        while(c % i == 0):
            count += 1
            c = c//i
        if i % 4 == 3 and count % 2 != 0:
            return False
        i += 1
    return c % 4 != 3

#Complexity:
#Time: O(sqrt(c))
#Space: O(1)

#Test Cases:
#5, 10064, 3, 18, 42

print(squareSumMethod1(5))
print(squareSumMethod2(5))

print(squareSumMethod1(10064))
print(squareSumMethod2(10064))

print(squareSumMethod1(3))
print(squareSumMethod2(3))

print(squareSumMethod1(18))
print(squareSumMethod2(18))

print(squareSumMethod1(42))
print(squareSumMethod2(42))