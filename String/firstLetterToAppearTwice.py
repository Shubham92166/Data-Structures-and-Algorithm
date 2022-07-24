def repeatedCharacter(s):
    d = {}
    for i in s:
        if d.get(i, -1) == -1:
            d[i] =  d.get(i, 0)+ 1
        else:
            return i

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"abccbaacz", "abcdd", "nwqusn"

print(repeatedCharacter("abcdd"))
print(repeatedCharacter("abccbaacz"))
print(repeatedCharacter("nwqusn"))
