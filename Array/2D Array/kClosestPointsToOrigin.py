import math
def kClosest(points, k):
    ans = []
    allDistances = []
    
    for point in points:
        distance = math.sqrt(pow(point[0], 2)+pow(point[1], 2))
        allDistances.append((distance, point))
    
    allDistances.sort(key = lambda x : x[0])
    
    for closestPoint in allDistances[:k]:
        ans.append(closestPoint[1])
    
    return ans

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[[1,3],[-2,2]], 1
#[[3,3],[5,-1],[-2,4]], 2

print(kClosest([[1,3],[-2,2]], 1))
print(kClosest([[3,3],[5,-1],[-2,4]], 2))

