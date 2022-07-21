def solve(A):
    d = {}
    for i in A:
        d[i] = d.get(i, 0) + 1
    if len(d) == 1:
        return 1
    oddCount = 0
    for value in d.values():
        if value % 2 != 0:
            oddCount += 1
            if oddCount > 1:
                return 0
    if len(A) % 2 == 0 and oddCount == 0:
        return 1
    elif len(A) % 2 != 0 and oddCount == 1:
        return 1
    else:
        return 0

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"abcde", "abbaee", "qhshkhygujljhoqzxn"

print(solve("abbaee"))
print(solve("abcde"))
print(solve("qhshkhygujljhoqzxn"))