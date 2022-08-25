import queue
def solve(A, B):
    q = queue.Queue()

    for i in A:
        q.put(i)

    current = 0
    cycleCount = 0
    while current < len(B):
        ele = q.get()
        while B[current]  != ele:
            q.put(ele)
            ele = q.get()
            cycleCount += 1
        
        current += 1
        
    return cycleCount+len(A)

#Complexity:
#Time: O(n^2)
#Space: O(n)

#Test Cases:
#[2, 3, 1, 5, 4], [1, 3, 5, 4, 2]
#[1], [1]

print(solve([2, 3, 1, 5, 4], [1, 3, 5, 4, 2]))
print(solve([1], [1]))