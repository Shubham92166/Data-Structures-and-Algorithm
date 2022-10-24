def countRightTriangles(A, B):
    points = list(zip(A, B))
    x_counts = {}
    y_counts = {}
    total = 0

    for i in points:
        x_counts[i[0]] = x_counts.get(i[0], 0)+1
        y_counts[i[1]] = y_counts.get(i[1], 0)+1

    for x, y in points:
        total += (x_counts[x]-1) * (y_counts[y]-1)

    return total % 1000000007

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[1, 1, 2], [1, 2, 1]
#[1, 1, 2, 3, 3], [1, 2, 1, 2, 1]

#Link: https://www.geeksforgeeks.org/count-of-right-angled-triangle-formed-from-given-n-points-whose-base-or-perpendicular-are-parallel-to-x-or-y-axis/
