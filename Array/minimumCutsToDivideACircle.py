def numberOfCuts(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return n//2
    else:
        return n

#Complexity:
#Time: O(1)
#Space: O(1)

#Test Cases:
#4, 3, 1

print(numberOfCuts(4))
print(numberOfCuts(3))
print(numberOfCuts(1))

#Link: https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/