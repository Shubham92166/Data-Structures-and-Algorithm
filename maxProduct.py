l=[1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21]
#Solution1
l.sort()
maxProduct=l[-1]*l[-2]
print(maxProduct)

#Solution2
maxProduct=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(maxProduct<l[i]*l[j]):
            maxProduct=l[i]*l[j]
print(maxProduct)