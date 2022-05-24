def letterCombinations(digits):
    if digits == '':
        return []
    if (digits) == 0:
        output = []
        output.append('')
        return output
    lastDigit = int(digits) % 10
    remainingDigits = letterCombinations(int(digits)//10)
    
    s = getStr(lastDigit)
    output = []
    for char in s:
        for digit in remainingDigits:
            output.append(digit+char)
    return output

def getStr(n):
    if n ==2:
        return "abc"
    elif n == 3:
        return "def"
    elif n == 4:
        return "ghi"
    elif n == 5:
        return "jkl"
    elif n == 6:
        return "mno"
    elif n == 7:
        return "pqrs"
    elif n == 8:
        return "tuv"
    elif n == 9:
        return "wxyz"
    else:
        return ''


#Test Cases:
# "", "2", "23", "745", "8543"

#Complexity:
#Time: O(N2)
#Space: O(N) # N is the length of the number

print(letterCombinations(""))
print(letterCombinations("23"))
print(letterCombinations("745"))
print(letterCombinations("8543"))

