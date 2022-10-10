def minimumPlatform(start,end):
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

#Complexity:
#Time: O(n)
#Space: O(1) 
#Since array size is fixed to 2361 and n is the size of array

#Test Cases:
#[900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]
#[900, 1100, 1235], [1000, 1200, 1240]

print(minimumPlatform([900, 940, 950, 1100, 1500, 1800], [910, 1200, 1120, 1130, 1900, 2000]))
print(minimumPlatform([900, 1100, 1235], [1000, 1200, 1240]))

#Link: https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1?page=2&curated[]=2&sortBy=submissions