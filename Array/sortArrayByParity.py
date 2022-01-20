def sortArrayByParity(arr):
    if(len(arr)==1):
        return arr
    i=0
    j=len(arr)-1
    while(i<j):
        if(arr[i]%2!=0 and arr[j]%2==0):
            arr[i], arr[j]= arr[j], arr[i]
            i+=1
            j-=1
        elif(arr[i]%2==0):
            i+=1
        elif(arr[j]%2!=0):
            j-=1
    return arr
arr=[1,2,4,6,5,7]
arr1=[7]
ans=sortArrayByParity(arr1)
print(ans)