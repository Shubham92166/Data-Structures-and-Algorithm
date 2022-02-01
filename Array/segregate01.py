def segregate0and1(arr):
    l, r = 0, len(arr)-1

    #l is the left pointer and r is the right pointer
    #We need to arrange the array in such a way that all 0's shift to the left and all 1's to the right
    #if lth index element is 0 and rth index element is 1 then we simply increment both the pointers\
    #else we swap them

    while(l<=r):
        if arr[l] == 0:
            l+=1
        elif arr[r] == 1:
            r-=1
        else:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1
    return arr

#Test case: [0,0,1,1,0], [1,1,1,1]

#Complexity:
#Time: O(N)
#Space: O(1)

print(segregate0and1([0,0,1,1,0]))
print(segregate0and1([1,1,1,1]))


