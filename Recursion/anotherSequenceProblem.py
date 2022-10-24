def solve(A):
    ans = calculate(A) 
    if A <= 2:
        return ans
    return ans

def calculate(A):
    if 1 <= A <= 2:
        return A
    if A == 0:
        return 1 
    return calculate(A-1) + calculate(A-2) + calculate(A-3) + A

#Complexity:
#Time: O(3^n)
#Space: O(n)

#Test Cases:
#3, 2

print(solve(3))
print(solve(2))

