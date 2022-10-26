def findMaxSum(arr, n):
    dp = [0]*(n+2)
    return helper(arr, 0, n, dp)
    
def helper(arr, i, n, dp):
    for i in range(n-1, -1, -1):
    
        ans1 = arr[i] + dp[i+2]
        ans2 = dp[i+1]
        dp[i] = max(ans1, ans2)
    
    return dp[0]

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[5, 5, 10, 100, 10, 5], 6
#[3, 2, 7, 10], 4

print(findMaxSum([5, 5, 10, 100, 10, 5], 6))
print(findMaxSum([3, 2, 7, 10], 4))

#Link: https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1?page=3&category[]=Dynamic%20Programming&sortBy=submissions