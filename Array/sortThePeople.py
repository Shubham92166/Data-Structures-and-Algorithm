def sortPeople(names, heights):
    val = list(zip(names, heights))
    ans =  sorted(val, reverse = True, key = lambda x: x[1])
    res = [i[0] for i in ans]
    return res

#Complexity:
#Time: O(n logn)
#Space: O(n)

#Test Cases:
#["Mary","John","Emma"], [180,165,170]
#["Alice","Bob","Bob"], [155,185,150]

print(sortPeople(["Mary","John","Emma"], [180,165,170]))
print(sortPeople(["Alice","Bob","Bob"], [155,185,150]))

#Link: https://leetcode.com/problems/sort-the-people/