def isCyclic(self, V, adj):
    adjList = {}
    for index in range(V):
        adjList[index] = adj[index]
    
    visited = [0]*(V)
    
    for source in range(V):
        if visited[source] == 0:
            if dfs(source, visited, adjList) == True:
                return 1
    return 0
        
def dfs(source, visited, adjList):
    visited[source] = 1
    for destination in adjList[source]:
        if visited[destination] == 0:
            dfs(destination, visited, adjList)
    
        if visited[destination] == 1:
            return True
    
    visited[source] = 2

#Complexity:
#Time: O(V+E)
#Space: O(V)
#Where V is the no. of vertices and E is the no. of Edges

#Link: https://practice.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

