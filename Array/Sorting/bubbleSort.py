def bubbleSort(A, n):
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if A[j+1] < A[j]:
                swapped = True
                A[j], A[j+1] = A[j+1], A[j]
        if not swapped:
            break
    return A

#Complexity:
#Time: O(N^2)
#Space: O(1)

#Test Case:
#[4, 1, 3, 9, 7], 5
#[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10

print(bubbleSort([4, 1, 3, 9, 7], 5))
print(bubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10))

#LInk: https://practice.geeksforgeeks.org/problems/bubble-sort/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article