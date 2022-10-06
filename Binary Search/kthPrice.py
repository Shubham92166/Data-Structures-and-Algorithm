def solve(A, B):
    minEle = min(A)
    maxEle = max(A)
    ans = -1
    ans = BS(A, minEle, maxEle, B)
    return ans

def BS(A, l, r, k):
    ans = -1
    while l <= r:
        mid = l + (r-l)//2
        count = countElements(A, mid)
        
        if count >= k:
            ans = mid
            r = mid-1
        else:
            l = mid+1
    return ans

def countElements(A, target):
    count = 0

    for i in A:
        if i <= target:
            count += 1
    
    return count

#Complexity:
#Time: O(n logn)
#Space: O(1)

#Test Cases:
#[2, 1, 4, 3, 2], 3

print(solve([2, 1, 4, 3, 2], 3))