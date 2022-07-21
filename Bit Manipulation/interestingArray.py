def solve(A):
    xor = 0
    for i in A:
        xor ^= i
    if xor % 2 == 0:
        return "Yes"
    else:
        return "No"  

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[9, 17], [1]

print(solve([1]))
print(solve([9, 17]))