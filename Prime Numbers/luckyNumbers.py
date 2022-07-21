def luckyNumbers(A):
    isPrime = [True] * (A+1)
    isPrime[0] = isPrime[1] = False
    counter = {}
    for i in range(0, A+1):
        counter[i] = 0
        
    i = 2
    while(i <= A):
        if isPrime[i]:
            for j in range(i, A+1, i):
                counter[j] = counter.get(j) + 1
                isPrime[j] = False
        i += 1
    
    count = 0
    for key, val in counter.items():
        if val == 2:
            count += 1
    return count

#Complexity:
#Time: O(nlogn)
#Space: O(n)

#Test Cases:
#8, 12, 1500

print(luckyNumbers(1500))
print(luckyNumbers(8))
print(luckyNumbers(12))

        