#You are given two strings, A and B, of size N and M, respectively.
#You have to find the count of all permutations of A present in B as a substring. You can assume a string will have only lowercase 
#letters.

def solve(A, B):
    dic1 = {}
    dic2 = {}
    count = 0
    n = len(A)

    for i in A:
        dic1[i] = dic1.get(i, 0)+1

    for i in range(len(A)):
        dic2[B[i]] = dic2.get(B[i], 0)+1
    count += check(dic1, dic2)

    k = 0
    for j in range(n, len(B)):
        dic2[B[j]] = dic2.get(B[j], 0) + 1
        dic2[B[k]] = dic2.get(B[k], 0) - 1
        if dic2[B[k]] == 0:
            del dic2[B[k]]
        k += 1
        count += check(dic1, dic2)
        
    return count

def check(dic1, dic2):
    count = 0
    flag = True
    for i in dic1:
        freq = dic1.get(i)
        if dic2.get(i) != freq :
            flag = False
            break
    if flag:
        count += 1
    return count

#Complexity:
#Time: O(m) 
#Space: O(m)
#m is the length of B

#Test Cases:
#"abc", "abcbacabc"
#"aca", "acaa"
#"p", "pccdpeeooadeocdoacddapacaecb"

print(solve("abc", "abcbacabc"))
print(solve("aca", "acaa"))
print(solve("p", "pccdpeeooadeocdoacddapacaecb"))