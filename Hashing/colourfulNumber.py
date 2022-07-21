def colourfulNumber(A):
    if A <= 9:
        return 1
    digits = []
    while(A):
        d = A%10
        if d <= 1:
            return 0
        digits.append(d)
        A //= 10
    if len(set(digits)) != len(digits):
        return 0
    dic = {}
    for i in digits:
        dic[i] = dic.get(i, 0) + 1

    for i in range(len(digits)):
        prod = digits[i]
        for j in range(i+1, len(digits)):
            prod *=  digits[j]
            if dic.get(prod, -1) != -1:
                return 0
            else:
                dic[prod] = 1
    return 1

#Complexity:
#ime: O(1)
#Space: O(1)

#Test Cases:
#3245, 236, 246

print(colourfulNumber(3256))
print(colourfulNumber(236))
print(colourfulNumber(246))

