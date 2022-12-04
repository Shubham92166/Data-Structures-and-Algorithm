def isCircularSentence(sentence):
    words = sentence.split()
    
    for i in range(len(words)-1):
        if words[i][-1] != words[i+1][0]:
            return False
    
    if words[-1][-1] != words[0][0]:
        return False
    
    return True

#Complexity:
#Time: O(n)
#Space: O(n)
#Where n is the no. of words in the sentence

#Test Cases:
#"leetcode exercises sound delightful", "eetcode", "Leetcode is cool"

print(isCircularSentence("leetcode exercises sound delightful"))
print(isCircularSentence("eetcode"))
print(isCircularSentence("Leetcode is cool"))

#Link: https://leetcode.com/problems/circular-sentence/