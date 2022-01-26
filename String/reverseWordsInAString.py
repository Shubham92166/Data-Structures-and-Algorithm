#Approach-1: Recursive

def recursiveReverseWord(s):
    s=s.split()
    length=len(s)
    if(length<=1):
        return s[0]
    res=reverse(s, 0, len(s)-1)
    return " ".join(s)

def reverse(s, start, end):
    if(start<end):
        s[start], s[end] = s[end], s[start]
        reverse(s,start+1, end-1)
    return s

#Complexity:
#Time: O(N)
#Space: O(N) for recursion stack

#Approach-2: Iterative
def iterativeReverseWord(s):   
    sl=s.split()
    if(len(s)==1):
        return s
    start=0
    end=len(sl)-1
    while(start<end):
        sl[start], sl[end] = sl[end], sl[start]
        start+=1
        end-=1
    return " ".join(sl)

#Complexity:
#Time: O(N)
#Space: O(1)

#Test Case: "  hello world  ", "a good   example", "the sky is blue", " Shubham ", "Shubham"

print(recursiveReverseWord(" Shubham "))
print(recursiveReverseWord("a good   example"))
print(iterativeReverseWord("Shubham"))
print(iterativeReverseWord("  hello world  "))

