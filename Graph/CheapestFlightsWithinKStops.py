import queue, math
import collections
from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = collections.defaultdict(list)
        for source, destination, cost in flights:

            adj_list[source].append([destination, cost])

        q = queue.Queue()
        q.put((0, src, 0))

        ans = [math.inf]*n

        ans[src] = 0

        while not q.empty():
            stops_taken, cur_node, cur_cost = q.get()

            if stops_taken > k:
                continue
            
            for neighbor, dest_cost in adj_list[cur_node]:

                if cur_cost + dest_cost < ans[neighbor] and stops_taken <= k:

                    ans[neighbor] = cur_cost + dest_cost
                
                    q.put((stops_taken + 1, neighbor, cur_cost + dest_cost))

        if ans[dst] != math.inf:
            return ans[dst]
        return -1


#Complexity:
#Time: O(V+E)
#Space: O(V)

#Test Cases:
#4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1
#3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1
#3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0

sol = Solution()
print(sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))

#Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/description/


        