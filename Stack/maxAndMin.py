def solve(A):
    n = len(A)
    NGL = [-1]*n
    stack = []
    for i in range(len(A)):
        while stack and A[stack[-1]] <= A[i]:
            stack.pop()
        if stack:
            NGL[i] = stack[-1]
        stack.append(i)
    
    NGR = [n]*n
    n = len(A)
    stack = []
    for i in range(len(A)-1, -1, -1):
        while stack and A[stack[-1]] <= A[i]:
            stack.pop()
        if stack:
            NGR[i] = stack[-1]
        stack.append(i)

    NSL= [-1]*n
    stack = []
    for i in range(len(A)):
        while stack and A[i] <= A[stack[-1]]:
            stack.pop()
        if stack:
            NSL[i] = stack[-1]
        stack.append(i)
    

    NSR= [n]*n
    stack = []
    for i in range(len(A)-1, -1, -1):
        while stack and A[i] <= A[stack[-1]]:
            stack.pop()
        if stack:
            NSR[i] = stack[-1]
        stack.append(i)

    ans = 0
    for i in range(len(A)):
        maxEle = (i-NGL[i])*(NGR[i]-i)*A[i]
        minELe = (i-NSL[i])*(NSR[i]-i)*A[i]
        ans += (maxEle - minELe)
    return ans % ((10**9)+7)

        
    return (maxEle - minELe) % ((10**9) + 7) 

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1], [4, 7, 3, 8]

print(solve([1]))
print(solve([4, 7, 3, 8]))