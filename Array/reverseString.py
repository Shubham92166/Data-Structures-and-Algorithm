#Approach-1: Iterative

def reverseStringIterative(s):
    i=0
    j=len(s)-1
    while(i<j):
        s[i], s[j] = s[j], s[i]
        i+=1
        j-=1
    return s

#Complexity: 
#Time: O(n)
#Space: O(1)

#Approach-2: Recursive:

def reverseStringRecursive(s):
    length=len(s)
    if(length<=1):
        return s
    res=reverse(s, 0, len(s)-1)
    return res
def reverse(s, start, end):
    if(start<end):
        s[start], s[end] = s[end], s[start]
        reverse(s,start+1, end-1)
    return s

#Complexity: 
#Time: O(n)
#Space: O(n) #for recursion stack

print(reverseStringIterative(["h","e","l","l","o"]))
print(reverseStringRecursive(["a","b"]))

#Test Case: ["h","e","l","l","o"], ["a","b"], ["H","a","n","n","a","h"]



 
