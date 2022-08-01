def solve(A):
    s = set()
    s.add(0)
    sum = 0
    for i in range(len(A)):
        sum += A[i]
        if sum in s:
            return True
        s.add(sum)
    return False

#Complexity:
#Time: O(n)
#Space: O(n)

#Test cases:
#[1, 2, 3, 4, 5], [1, -1], [4, 2, -3, 1, 6], [4, 2, 0, 1, 6], [-3, 2, 3, 1, 6]

print(solve([1, 2, 3, 4, 5]))
print(solve([1, -1]))
print(solve([4, 2, -3, 1, 6]))
print(solve([4, 2, 0, 1, 6]))
print(solve([-3, 2, 3, 1, 6]))

#Link: https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/