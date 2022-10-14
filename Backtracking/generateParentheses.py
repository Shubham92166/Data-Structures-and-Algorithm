def generateParenthesis(n):
    ans = []
    return helper(n*2, ans, "", 0, 0)

def helper(n, ans, pos, open, close):
    if n == 0:
        if open == close:
            ans.append(pos)
        return 
    
    if open < close:
        return
    
    helper(n-1, ans, pos+"(", open+1, close)
    helper(n-1, ans, pos+")", open, close+1)
    return ans

#Complexity:
#Time: O(2^n)
#Space: O(n)

#Test Cases:
#3, 1, 8

print(generateParenthesis(3))
print(generateParenthesis(1))
print(generateParenthesis(8))

#Link: https://leetcode.com/problems/generate-parentheses/