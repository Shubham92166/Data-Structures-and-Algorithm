def divide(dividend, divisor):    
    result = 0
    sign = 1
    
    if (dividend >= 0 and divisor < 0) or (dividend <= 0 and divisor > 0):
        sign = -1
    
    dividend = abs(dividend)
    divisor = abs(divisor)
    
    while dividend - divisor >= 0:
        count = 0
        while dividend - (divisor << 1 << count) >= 0:
            count += 1
        
        result += 1 << count
        
        dividend -= divisor << count
        
    result *= sign
    
    if result > (1 << 31)-1:
        return (1 << 31)-1
    elif result < -(1 << 31):
        return -(1 << 31)
    else:
        return result

#Complexity:
#Time: O(log^2 n)
#Space: O(1)

#Test Cases:
#10, 3
#7, -3

print(divide(10, 3))
print(divide(7, -3))

#Link: https://leetcode.com/problems/divide-two-integers/