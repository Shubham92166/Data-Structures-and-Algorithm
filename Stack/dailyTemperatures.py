def dailyTemperatures(nums):
    stack = []
    ans = [0]*len(nums)
    for i, v in enumerate(nums):
        while stack and stack[-1][1] < v:
            index, value = stack.pop()
            ans[index] = i-index
        stack.append([i, v])
    return ans

#Complexity:
#Time: O(n)
#Space: O(1) #if we ignore the output array

#Test Cases:
#[73,74,75,71,69,72,76,73], [30,40,50,60], [30,60,90]

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))

#Link: https://leetcode.com/problems/daily-temperatures/