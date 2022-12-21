def generate(numRows):
    pascal = [[1], [1,1]]

    if numRows == 1:
        return [pascal[0]]
    
    elif numRows == 2:
        return pascal
    
    i = 1

    while i+1 < numRows:
        i += 1
        pascal.append([1])
        for j in range(len(pascal[i-1])-1):
            pascal[i].append(pascal[i-1][j+1] + pascal[i-1][j])
        pascal[i].append(1)
    
    return pascal

#Complexity:
#Time: O(n^2)
#Space: O(n^2)

#Test Cases:
#1, 2, 8, 30

print(generate(1))
print(generate(2))
print(generate(8))
print(generate(30))

#Link: https://leetcode.com/problems/pascals-triangle/description/
