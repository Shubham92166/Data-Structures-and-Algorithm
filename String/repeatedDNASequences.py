'''
Approach: We can use here sliding window algorithm as we need to check the 10 length string only. We create a window of 10 length and 
add it a unique hashset. Now, we traverse the given string and for every window we check whether it has already been occured or not by 
checking in unique hashet. If it has already occured means it is repeated sequence so we store it in duplicate hashset. At the end, all 
the unique repeated sequence will be stored in duplicate hashset so we return it as our final answer.
'''

def findRepeatedDnaSequences(s):
    unique = set()
    duplicate = set()
    
    window = s[:10]  
    
    unique.add(window)
    
    for i in range(10, len(s)):
        window = window[1:]
        window += s[i]
        
        if window in unique:
            duplicate.add(window)
        
        else:
            unique.add(window)
            
    return duplicate

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", "AAAAAAAAAAAAA"

print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))

#Link: https://leetcode.com/problems/repeated-dna-sequences/
