import queue, collections

def canFinish(C, prerequisites):
    adjList = collections.defaultdict(list)
    
    for pair in prerequisites:
        adjList[pair[1]].append(pair[0])
    
    inc = [0]*(C)
    for source in range(C):
        for node in adjList[source]:
            inc[node] += 1
    
    q = queue.Queue()

    for i in range(C):
        if inc[i] == 0:
            q.put(i)
    
    ans = []
    while not q.empty():
        node = q.get()
        ans.append(node)
        for adj in adjList[node]:
            inc[adj] -= 1 
            if inc[adj] == 0:
                q.put(adj)

    if len(ans) == C:
        return True
    return False

#Complexity:
#Time: O(V+E)
#Space: O(V)

#Test Cases:
#2, [[1,0]]
#2, [[1,0],[0,1]]

print(canFinish(2, [[1,0]]))
print(canFinish(2, [[1,0],[0,1]]))

#Link: https://leetcode.com/problems/course-schedule/