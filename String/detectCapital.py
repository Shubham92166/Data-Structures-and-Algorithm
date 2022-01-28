def detectCapital(word):
    flag=False
    if(len(word)==1):
        return True
    if ord(word[0])>=65 and ord(word[0])<=90 and 65<=ord(word[1])<=90:
        if(len(word)==2):
            return True
        for char in range(2, len(word)):
            if 65<=ord(word[char])<=90:
                flag=True
            else:
                flag=False
                break
    elif(97<=ord(word[0])<=122 or 65<=ord(word[0])<=90):
        for char in range(1, len(word)):
            if(97<=ord(word[char])<=122):
                flag=True
            else:
                flag=False
                break          
    return flag

#-------------More optimized code---------------#

def optimizedDetectCapital(word):
    count=0
    for char in range(len(word)):
        if 65<=ord(word[char])<=90:
            count+=1
    if(count==0):
        return True
    elif(count==1 and 65<=ord(word[0])<=90):
        return True
    elif(count==len(word)):
        return True
    return False

print(detectCapital("USA"))
print(optimizedDetectCapital("flaG"))
