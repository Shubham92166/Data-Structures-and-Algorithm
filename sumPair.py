#Solution1
from itertools import permutations
l=[2,6,3,9,11]
target=9
permutation=permutations(l,2)
for pair in permutation:
    if(sum(pair)==target and pair[0]!=pair[1]):
        print(pair)

#Solution2
for i in range(len(l)):
    for j in range(1,len(l)):
        if(l[i]!=l[j]and l[i]+l[j]==target):
            print((l[i],l[j]), end=",")