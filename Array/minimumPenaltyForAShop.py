import math 

def bestClosingTime(customers):
    length = len(customers)
    arr = [0]*(length+1)
    
    totalCountOfY = 0
    totalCountOfN = 0
    
    for visit in customers:
        if visit == 'Y':
            totalCountOfY += 1
        else:
            totalCountOfN += 1
    
    currentCountOfY = 0
    currentCountOfN = 0
    
    arr[0] = totalCountOfY
    
    for i in range(1, length):
        if customers[i-1] == 'Y':
            currentCountOfY += 1
            arr[i] = totalCountOfY - currentCountOfY + currentCountOfN
        else:
            currentCountOfN += 1
            arr[i] = totalCountOfY - currentCountOfY + currentCountOfN
    
    arr[length] = currentCountOfN
    
    earliestHour = 0
    minPenalty = math.inf
        
    for i in range(length+1):
        if arr[i] < minPenalty:
            earliestHour = i
            minPenalty = arr[i]
    
    return earliestHour

#Complexity:
#Time: O(n)
#SPace: O(n)
#Where n is the length of the given array

#Test Cases:
#"YYNY", "NNNNN", "YYYY"

print(bestClosingTime("YYNY"))
print(bestClosingTime("NNNNN"))
print(bestClosingTime("YYYY"))

#Link: https://leetcode.com/problems/minimum-penalty-for-a-shop/