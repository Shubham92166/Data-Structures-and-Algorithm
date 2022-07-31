#Concept: Minimum no. of rooms = maximum no. of classes scheduled at a given time. 
#Note: If start and end time is not given in sorted order then sort them individually

def minimumRooms(start, end):
    meet = [0] * 2361
    
    for i in range(len(start)):
        meet[start[i]] += 1
        meet[end[i]+1] -= 1

    maxEle = meet[0]

    for i in range(1, 2361):
        meet[i] = meet[i] + meet[i-1]
    
    for i in range(1, 2361):
        maxEle = max(maxEle, meet[i])
    return maxEle

#Time: O(n)
#Space: O(n)

#Test Cases:
#[0900, 1100, 1235], [1000, 1200, 1240]
#[0900, 0940, 0950, 1100, 1500, 1800], [0910, 1200, 1120, 1130, 1900, 2000]

print(minimumRooms([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))
print(minimumRooms([900, 1100, 1235], [1000, 1200, 1240]))

#Link: https://practice.geeksforgeeks.org/contest/interview-series-61/problems/#