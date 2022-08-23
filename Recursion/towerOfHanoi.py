def towerOfHanoi(A):
        steps = []
        solve(A, 1, 2, 3, steps)
        return steps
    
def solve( n, src, temp, dest, steps):
    if n == 0:
        return 
    solve(n-1, src, dest, temp, steps)
    steps.append([n, src, dest])
    solve(n-1, temp, src, dest, steps)

#Complexity:
#Time: O(2^n)
#Space: O(n)

#Test Cases:
#2, 3, 18

print(towerOfHanoi(2))
print(towerOfHanoi(3))
print(towerOfHanoi(18))
