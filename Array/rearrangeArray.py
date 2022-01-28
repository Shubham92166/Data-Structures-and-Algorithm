def Rearrange (arr,  n) : 
    i=0
    while(i<n):
        if(arr[i]>=0 and arr[i]!=i):
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        else:
            
            i+=1
    return arr

#Test Case: [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1], [2, 0, 1]

#Complexity:
#Time: O(n)
#Space: O(1)

print(Rearrange([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1], len([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1])))