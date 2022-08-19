def calculateTax(brackets, income):
    tax = 0
    if income >= brackets[0][0]:
        tax += brackets[0][0]*(brackets[0][1]/100)
        income -= brackets[0][0]
    else:
        tax += income * (brackets[0][1]/100)
        income = 0
        return tax
    for i in range(1, len(brackets)):
        value = brackets[i][0]-brackets[i-1][0]
        if value < income:
            tax += value * (brackets[i][1]/100)
            income -= value
        else:
            tax += income*(brackets[i][1]/100)
            return tax
    return tax

#Complexity:
#Time: O(n)
#Space: O(1)
#Since each row has only two columns which is constant. Thus, time complexity is O(2n) i.e., O(n)

#Test Cases:
#[[3,50],[7,10],[12,25]], 10
#[[1,0],[4,25],[5,50]], 2
#[[2,50]], 0
#[[2,28]], 1

print(calculateTax([[3,50],[7,10],[12,25]], 10))
print(calculateTax([[1,0],[4,25],[5,50]], 2))
print(calculateTax([[2,50]], 0))
print(calculateTax([[2,28]], 1))

