#Approach: We are taking a hashmap and ans variable whose initial value is infinite. We store each element as a key and it's index as value. When the current element is not in hashmap
#then we add it to the hashmap with it's index. If it already exists means it was found before and thus, we found two elements whose 
#indexes are different and values are same. So, we take the absolute value of their indexes and store the minimum value so far in ans
#variable. We do it for all the elements of the array. If at the end, the ans variable still holds infinite value that means no pair was
#found so we can return -1 else whatever value we have in ans variable.
import math
def solve(A):
    dic = {}
    ans = math.inf
    for i in range(len(A)):
        if A[i] not in dic:
            dic[A[i]] = i 
        else:
            ans = min(ans, abs(dic[A[i]]-i))
    if ans == math.inf:
        return -1
    return ans

#Complexity: O(n)
#Space: O(1)

#Test Cases:
#[7, 1, 3, 4, 1, 7], [1, 1]

print(solve([7, 1, 3, 4, 1, 7]))
print(solve([1, 1]))