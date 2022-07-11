def merge(A):
    A.sort(key = lambda x: x[0])
    index = 0
    for i in range(1, len(A)):
        if A[index][1] >= A[i][0]:
            A[index][1] = max(A[index][1], A[i][1])
        else:
            index += 1
            A[index] = A[i]
    return A[:index+1]

#Complexity:
#Time: O(nlogn)
#Space: O(1)

#Test Cases:
#[[1,3],[2,6],[8,10],[15,18]]
#[[1,3],[3,6],[6,8],[8,9]]
#[[1,4],[4,5]]

print(merge([[1,4],[4,5]]))
print(merge([[1,3],[3,6],[6,8],[8,9]]))
print(merge([[1,3],[2,6],[8,10],[15,18]]))