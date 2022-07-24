def equalPairs(grid):
    count = 0
    row = []
    col = []
    for i in range(len(grid)):
        row.append(grid[i])
    for i in range(len(grid)):
        temp = []
        for j in range(len(grid)):
            temp.append(grid[j][i])
        col.append(temp)
    for i in row:
        for j in col:
            if i == j:
                count += 1
    return count

#Complexity:
#Time: O(n^2)
#Space: O(n)

#Test Cases:
#[[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], [[3,2,1],[1,7,6],[2,7,7]]

print(equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))