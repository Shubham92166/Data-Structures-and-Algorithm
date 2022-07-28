#Get the maximum number of "Balloon" word from the given string s
def maxInstance(s):
    dic = {}
    for i in s:
        dic[i] = dic.get(i, 0)+1
    return min(dic["b"], dic["a"], dic["n"], dic["l"] // 2, dic["o"] // 2)
    
    
#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#aonnollnmlmnoambanoamlmanll, loonbalxballpoon, nlaebolko, bnlbllanmbaamnmobbanablboolonlol

print(maxInstance("nlaebolko"))
print(maxInstance("loonbalxballpoon"))
print(maxInstance("aonnollnmlmnoambanoamlmanll"))
print(maxInstance("bnlbllanmbaamnmobbanablboolonlol"))

#Link: https://practice.geeksforgeeks.org/contest/interview-series-58/problems/#