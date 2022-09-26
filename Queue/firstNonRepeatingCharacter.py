import collections

class Solution:
    def solve(self, A):
        deq = collections.deque()
        ans = ""
        dic = {}
        for i in A:
            dic[i] = dic.get(i, 0) + 1
            deq.append(i)
            while deq and dic[deq[0]] > 1:
                deq.popleft()
            
            if deq:
                ans += deq[0]
            else:
                ans += "#"
        
        return ans

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
"abadbc", "abcabc"

sol = Solution()

print(sol.solve("abadbc"))
print(sol.solve("abcabc"))

#Link: https://www.interviewbit.com/problems/first-non-repeating-character-in-a-stream-of-characters/