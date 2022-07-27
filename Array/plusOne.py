def plusOne(digits):
    carry=0

    #We will add 1 only to the last index integer. So, in order to check that we are putting a condition whether the current index 
    #value is the last index value. If yes, then we will add 1 to it and carry will be put forward. else we will just add carry and 
    #cuurent index value

    for index in range(len(digits)-1,-1,-1):
        if(index==len(digits)-1):
            sum=digits[index]+1
        else:
            sum=digits[index]+carry
        digits[index]=sum%10
        carry=sum//10
    
    #in case we still have carry and the loop is over then we will need to put carry at the start of the array

    if(carry==1):
        digits.insert(0, carry)
    return digits

#Test case: [1,2,3], [4,3,2,1], [9], [9,9,9]

#Complexity:
#Time: O(n)
#Space: O(1)

print(plusOne([9,9,9]))
print(plusOne([9]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))

#Link: https://leetcode.com/problems/plus-one/
