import math
def firstRep(s):
    dic = {}
    ans = math.inf
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = i
        else:
            ans = min(ans, dic[s[i]])
    if ans == math.inf:
        return -1
    return s[ans]

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"go", "hellhooo", "geeksforgeeks"

print(firstRep("geeksforgeeks"))
print(firstRep("hellhooo"))
print(firstRep("go"))