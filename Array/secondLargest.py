import math

def print2largest(arr, n):	
    firstLargest, secondLargest = -math.inf, -math.inf

    for index in range(n):
        if firstLargest < arr[index]:
            secondLargest = firstLargest
            firstLargest = arr[index]
        
        elif arr[index] > secondLargest and arr[index] != firstLargest:
            secondLargest = arr[index]
        
    return secondLargest if secondLargest != -math.inf else -1

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[12, 35, 1, 10, 34, 1], 6
#[10, 5, 10], 3
#[40, 40], 2

print(print2largest([12, 35, 1, 10, 34, 1], 6))
print(print2largest([10, 5, 10], 3))
print(print2largest([40, 40], 2))

#Link: https://practice.geeksforgeeks.org/problems/second-largest3735/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article