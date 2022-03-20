#Aprroach-1: Sorting both the arrays

def intersection(arr1, arr2):
    arr1.sort()
    arr2.sort()
    i, j, res = 0, 0, set()
    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i] == arr2[j]):
            res.add(arr1[i])
            i+=1
            j+=1
        elif(arr1[i]<arr2[j]):
            i+=1
        elif(arr2[j]<arr1[i]):
            j+=1
    return res


#Approach-2: Improved time complexity(sorted array having smaller size)

def intersection(arr1, arr2):
    ans = set()
    if(len(arr1)<=len(arr2)):
        arr1.sort()
    else:
        arr2.sort()
    if(arr1[0]<=arr1[-1]):
        for num in arr1:
            foundValue = searchPair(arr2, num)
            if(foundValue == num):
                ans.add(num)
        return ans
    elif(arr2[0]<=arr2[-1]):
        for num in arr2:
            foundValue = searchPair(arr1, num)
            if(foundValue == num):
                    ans.add(num)
        return ans

#Searching for current element of one list in another list using Binary Search Algorithm
       
def searchPair(self, nums, element):
    l, r = 0, len(nums)-1
    while(l<=r):
        mid = (l+r)//2
        if(nums[mid] == element):
            return nums[mid]
        elif(nums[mid]>element):
            r = mid-1
        else:
            l = mid+1
    return -1

#Link: https://leetcode.com/problems/intersection-of-two-arrays/


