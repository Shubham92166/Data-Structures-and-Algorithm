import collections, math
from heapq import *

def networkDelayTime(times, n, k):
    adjList = collections.defaultdict(list)
    
    for source, destination, time in times:
        adjList[source].append((destination, time))
        
    t = [math.inf]*(n+1)
    visited = [0]*(n+1)
    
    bfs(k, adjList, t, visited)
    
    maxTime = max(t[1:])
    
    if maxTime == math.inf:
        return -1
    
    return maxTime
    
def bfs(source, adjList, t, visited):
    heap = [[0, source]]
    t[source] = 0
    heapify(heap)
    
    while heap:
        time, node = heappop(heap)
        for dest, tim in adjList[node]:
            if t[dest] > time+tim:
                t[dest] = min(t[dest], tim+time)
                heappush(heap, [t[dest], dest])

#Complexity:
#Time: O(V+E)
#Space: O(V)
#Where V is the no. of vertices and E is the no. of Edges

#Test Cases:
#[[2,1,1],[2,3,1],[3,4,1]], 4, 2
#[[1,2,1]], 2, 1
#[[1,2,1]], 2, 2

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
print(networkDelayTime([[1,2,1]], 2, 1))
print(networkDelayTime([[1,2,1]], 2, 2))

#Link: https://leetcode.com/problems/network-delay-time/
