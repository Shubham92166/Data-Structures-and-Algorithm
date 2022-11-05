import queue, collections

def validPath(n, edges, source, destination):
    adjList = collections.defaultdict(list)

    for s, d in edges:
        adjList[s].append(d)
        adjList[d].append(s)

    return bfs(source, destination, adjList, n)

def bfs(source, dest, adjList, n):
    q = queue.Queue()
    q.put(source)
    
    visited = [False]*n
    
    visited[source] = True
    
    while not q.empty():
        v = q.get()
        
        if v == dest:
            return True 
        
        visited[v] = True
        
        for u in adjList[v]:
            if u == dest:
                return True
            
            if visited[u] == False:
                q.put(u)

    return False

#Complexity:
#Time: O(V+E)
#Space: O(V)

#Test Cases:
#3, [[0,1],[1,2],[2,0]], 0, 2
#6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5

print(validPath(3, [[0,1],[1,2],[2,0]], 0, 2))
print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))

#Link: https://leetcode.com/problems/find-if-path-exists-in-graph/
        