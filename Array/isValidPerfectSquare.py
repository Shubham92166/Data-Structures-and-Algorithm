def isPerfectSquare(num: int):
        l, r = 1, num
        while(l<=r):
            mid = (l+r)//2
            square = mid*mid
            if(square==num):
                return True
            elif(square>num):
                r = mid-1
            else:
                l = mid+1
        return False
#Test Cases: 16, 14, 100, 26, 5, 25 

#Complexity:
#Time: O(log n)
#Space: O(1) 

print(isPerfectSquare(16))
print(isPerfectSquare(14))
print(isPerfectSquare(100))
print(isPerfectSquare(26))
print(isPerfectSquare(5))