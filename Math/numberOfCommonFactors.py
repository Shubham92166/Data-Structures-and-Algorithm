def commonFactors(a, b):
    count = 0
    minVal = min(a, b)
    
    for i in range(1, minVal+1):
        if a%i == 0 and b % i == 0:
            count += 1
    
    return count

#Complexity:
#Time: O(min(n1,n2))
#Space: O(1)

#Test Cases:
#12, 6
#25, 30

print(commonFactors(12, 6))
print(commonFactors(25, 30))

#Link: https://leetcode.com/problems/number-of-common-factors/
