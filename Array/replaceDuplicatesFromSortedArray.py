#Replace all duplicates with zero and move them to the left.

def replaceDuplicates(arr):
    unique_element = arr[0]
    count = 0
    for i in range(1, len(arr)):
        if arr[i] == unique_element:
            arr[i] = None
            count += 1
        else:
            unique_element = arr[i]

    newArray = [0]*len(arr)
    for i in range(len(arr)):
        if arr[i] != None:
            newArray[count] = arr[i]
            count += 1
    return newArray

#Test Case: [-2,-2,-1,0,1,1,2,2,3,4], [0,0,0,0,0,0]

#Complexity:
#Time: O(n)
#Space: O(n)

arr1 = [-2,-2,-1,0,1,1,2,2,3,4]
print(replaceDuplicates(arr1))

arr2 = [0,0,0,0,0,0]
print(replaceDuplicates(arr2))



