#Approach-1: Using recursion

def firstCapital(word):
    if(65<=ord(word[0])<=90):
        return word[0]
    return firstCapital(word[1:])
    
#Test Case: "Shubham", januaRy", "computeR"

#Complexity:
#Time: O(n)
#Space: O(n) #for recursion stack

string="shubhaM"
print(firstCapital(string))