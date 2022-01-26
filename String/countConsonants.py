#Approach-1: Using Recursion

count=0
def countConsonants(word):
    global count
    if(len(word)>=1  and word[0] not in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]):
        count+=1 
    if(len(word)==0):
        return count
    return countConsonants(word[1:])

#Test Case: "Test", "AAa", "UAS"

#Complexity:
#Time: O(n)
#Space: O(n) # for recusion stack

print(countConsonants("UAS")) 