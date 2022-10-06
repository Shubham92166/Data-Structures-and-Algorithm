import math
def minimizedMaximum(n, quantities):
    l = 1
    r = max(quantities)
    ans = math.inf
    
    while l <= r:
        mid = l+(r-l)//2
        storesCount = countStore(quantities, mid)
        
        if storesCount > n:
            l = mid+1 
        else:
            r = mid-1
            ans = min(ans, mid) 

    return ans

def countStore(q, target):
    sum = 0
    
    for i in range(len(q)):
        sum += math.ceil(q[i]/target)
    
    return sum

#Complexity:
#Time: O(n logn)
#Space: O(1)

#Test Cases:
#6, [11,6]
#7, [15,10,10]
#1, [100000]

print(minimizedMaximum(6, [11,6]))
print(minimizedMaximum(7, [15,10,10]))
print(minimizedMaximum(1, [100000]))

#Link: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/