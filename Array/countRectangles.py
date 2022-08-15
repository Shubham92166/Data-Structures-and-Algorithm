def solve(A, B):
    points = set(zip(A, B))
    count = 0
    for x1, y1 in points:
        for x2, y2 in points:
            if x1 == x2 or y1 == y2:
                continue
            if (x1, y2) in points and (x2, y1) in points:
                count += 1
    return count//4

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1, 1, 2, 2], [1, 2, 1, 2]
#[1, 1, 2, 2, 3, 3], [1, 2, 1, 2, 1, 2]

print(solve([1, 1, 2, 2], [1, 2, 1, 2]))
print(solve([1, 1, 2, 2, 3, 3], [1, 2, 1, 2, 1, 2]))