import queue, collections

def findOrder(numCourses, prerequisites):
    adjList = collections.defaultdict(list)
    
    for pair in prerequisites:
        adjList[pair[1]].append(pair[0])
    
    inc = [0]*(numCourses)
    for source in range(numCourses):
        for node in adjList[source]:
            inc[node] += 1
    
    q = queue.Queue()

    for i in range(numCourses):
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

    if len(ans) == numCourses:
        return ans
    return []

#Complexity:
#Time: O(V+E)
#Space: O(V)

#Test Cases:
#2, [[1,0]]
#4, [[1,0],[2,0],[3,1],[3,2]]
#1, []

print(findOrder(2, [[1,0]]))
print(findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(findOrder(1, []))

#Link: https://leetcode.com/problems/course-schedule-ii/