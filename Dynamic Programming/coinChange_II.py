def change(amount, coins):
    n = len(coins)
    
    return helper(coins, amount, 0, n)

def helper(A, target, i, n):
    prev = [0]*(target+1)
    prev[0] = 1
    for i in range(n-1, -1, -1):
        cur = [0]*(target+1)
    
        for j in range(target+1):
            take = 0
            if j - A[i] >= 0:
                take = cur[j-A[i]]
            notTake = prev[j]
            cur[j] = take + notTake
        prev = cur

    return cur[target]