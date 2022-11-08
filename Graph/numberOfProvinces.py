import queue, collections

def findCircleNum(isConnected):
    adjList = collections.defaultdict(list)
    n = len(isConnected)
    for i in range(n):
        for j in range(n):
            if isConnected[i][j] == 1:
                adjList[i].append(j)
                adjList[j].append(i)
                
    connectedComponents = 0
    
    visited = [False]*(n)
    
    for i in range(n):
        if not visited[i]:
            connectedComponents += bfs(i, n, adjList, visited)
    
    return connectedComponents

def bfs(source, destination, adjList, visited):
    q = queue.Queue()
    q.put(source)
    visited[source] = True
    
    while not q.empty():
        node = q.get()
        
        if node == destination:
            return 0
        
        for adj in adjList[node]:
            if visited[adj] == False:
                visited[adj] = True
                q.put(adj)
    return 1

#Complexity:
#Time: O(V+E)
#Space: O(V)
#Where V is the no. of vertices and E is the no. of Edges in the given graph

#Test Cases:
#[[1,1,0],[1,1,0],[0,0,1]], [[1,0,0],[0,1,0],[0,0,1]]

print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
print(findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))
            
#Link: https://leetcode.com/problems/number-of-provinces/
            