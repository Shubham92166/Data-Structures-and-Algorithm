import queue, collections, math
from heapq import *

def solve(A, B, C):
    adjList = collections.defaultdict(list)

    for source, destination, weight in B:
        adjList[source].append((destination, weight))
        adjList[destination].append((source, weight))
    
    d = [math.inf]*A 

    bfs(C, A, adjList, d)

    for i in range(A):
        if d[i] == math.inf:
            d[i] = -1
    return d
        
def bfs(source, destination, adjList, d):
    
    heap = [[0, source]]
    d[source] = 0
    heapify(heap)

    while heap:
        weight, node = heappop(heap)
        
        for destination, w in adjList[node]:
            if d[destination] > weight+w:
                d[destination] = min(d[destination], weight+w)
                heappush(heap, [d[destination], destination])

#Complexity:
#Time: O(V+E)
#Space: O(V)
#Where V is the no. of vertices and E is the no. of Edges

#Test Cases:
#6, [[0, 4, 9], [3, 4, 6], [1, 2, 1], [2, 5, 1], [2, 4, 5], [0, 3, 7], [0, 1, 1], [4, 5, 7], [0, 5, 1]], 4
#5, [[0, 3, 4], [2, 3, 3], [0, 1, 9], [3, 4, 10], [1, 3, 8]], 4

print(solve(6, [[0, 4, 9], [3, 4, 6], [1, 2, 1], [2, 5, 1], [2, 4, 5], [0, 3, 7], [0, 1, 1], [4, 5, 7], [0, 5, 1]], 4))
print(solve(5, [[0, 3, 4], [2, 3, 3], [0, 1, 9], [3, 4, 10], [1, 3, 8]], 4))

#Link: https://practice.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article