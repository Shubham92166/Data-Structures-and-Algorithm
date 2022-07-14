def kthGrammar(n, k):
    if calculate(n, k) == True:
        return 1
    else:
        return 0

def calculate(n, k):
    if n == 1:
        return 0
    elif k % 2 == 0:
        return not calculate(n-1, k//2)
    else:
        return calculate(n-1, (k+1)//2)
    

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#30, 4566
#25, 67974

print(kthGrammar(30, 4566))
print(kthGrammar(25, 67974))