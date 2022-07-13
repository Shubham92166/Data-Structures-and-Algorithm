def countSquares(N):
    l = 0
    r = N
    while(l <= r):
        mid = l + (r-l)//2
        square = mid*mid
        if square == N:
            return mid-1
        elif square > N:
            r = mid-1
        else:
            l = mid+1
    return l-1


#Complexity:
#Time: O(log N)
#Time: O(1)

#Test Cases:
#1, 13, 7, 5, 28 

print(countSquares(1))
print(countSquares(13))
print(countSquares(7))
print(countSquares(5))
print(countSquares(28))