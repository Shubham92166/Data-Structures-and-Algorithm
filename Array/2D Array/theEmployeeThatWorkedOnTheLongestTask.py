import math
def hardestWorker(n, logs):
    longestTime = -math.inf
    ansId = math.inf
    prevEndTime = 0
    for log in logs:
        timeTaken = log[1]-prevEndTime
        if timeTaken > longestTime:
            ansId = log[0]
            longestTime = timeTaken
        elif timeTaken == longestTime:
            if log[0] < ansId:
                ansId = log[0] 
        prevEndTime = log[1]
    return ansId

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#10, [[0,3],[2,5],[0,9],[1,15]]
#26, [[1,1],[3,7],[2,12],[7,17]]
#2, [[0,10],[1,20]]

print(hardestWorker(10, [[0,3],[2,5],[0,9],[1,15]]))
print(hardestWorker(26, [[1,1],[3,7],[2,12],[7,17]]))
print(hardestWorker(2, [[0,10],[1,20]]))

#Link: https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/