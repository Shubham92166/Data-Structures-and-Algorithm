import queue

def isCycle(V, adj):
    visited = [False]*(V +1)
    for vertex in range(V):
        if not visited[vertex]: 
            if bfs(vertex, V, adj, visited) == True:
                return 1
    return 0
    
def bfs(source, destination, adjList, visited):
    q = queue.Queue()

    q.put((source, -1))
    visited[source] = True

    while not q.empty():
        node, parent = q.get()

        for adj in adjList[node]:
            if visited[adj] == False:
                visited[adj] = True
                q.put((adj, node))
            else:
                if adj != parent:
                    return True
    return False

#Complexity:
#Time: O(V+E)
#Space: O(V)

#Test Cases:
#5, [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]] 
#4, [[], [2], [1, 3], [2]]

print(isCycle(5, [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]))
print(isCycle(4, [[], [2], [1, 3], [2]]))

#Link: https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
