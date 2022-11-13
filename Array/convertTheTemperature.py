def convertTemperature(celsius):
    return [celsius+273.15, celsius*1.80+32.00]
        
#Complexity:
#Time: O(1)
#Space: O(1)

#Test Cases:
#36.50, 122.11

print(convertTemperature(36.50))
print(convertTemperature(122.11))

#Link: https://leetcode.com/problems/convert-the-temperature/