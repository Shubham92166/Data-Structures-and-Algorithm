def sortedSquares(nums):        
    i, j= 0, len(nums)-1
    res=[0]*(len(nums))
    k=len(nums)-1
    arr=[ele**2 for ele in nums]
    while(i<=j):
        if(arr[i]<=arr[j]):
            res[k]=arr[j]
            j-=1
        elif(arr[i]>arr[j]):
            res[k]=arr[i]
            i+=1 
        k-=1
    return res

#Test Cases: [-4,-1,0,3,10], [-7,-3,2,3,11]

#Complexity:
#Time: O(N)
#Space: O(N)

print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))