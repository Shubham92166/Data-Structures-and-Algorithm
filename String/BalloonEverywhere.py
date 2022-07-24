#Get the maximum number of "Balloon" word from the given string s
def maxInstance(s):
    dic = {}
    for i in s:
        dic[i] = dic.get(i, 0)+1
    possibility = min(dic["b"], dic["a"], dic["n"])
    if  dic["l"] >= 2*possibility and  dic["o"] >= 2*possibility:
        return possibility
    else:
        return min(dic["l"] // 2, dic["o"] // 2)
    
#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#aonnollnmlmnoambanoamlmanll, loonbalxballpoon, nlaebolko

print(maxInstance("nlaebolko"))
print(maxInstance("loonbalxballpoon"))
print(maxInstance("aonnollnmlmnoambanoamlmanll"))