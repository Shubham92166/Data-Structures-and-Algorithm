def dividePlayers(skill):
    n = len(skill)
    groups = n//2
    
    sortedSkills = sorted(skill)
    
    start = 0
    end = n-1
    
    minValue = sortedSkills[0]
    maxValue = sortedSkills[-1]
    
    target = minValue + maxValue
    
    sumOfChem = 0
    
    while start < end:
        if sortedSkills[start] + sortedSkills[end] != target:
            return -1
        sumOfChem += sortedSkills[start]*sortedSkills[end]
        start += 1
        end -= 1
    
    return sumOfChem

#Complexity:
#Time: O(n logn)
#Space: O(n)

#Test Cases:
#[3,2,5,1,3,4], [3,4], [1,1,2,3]

print(dividePlayers([3,2,5,1,3,4]))
print(dividePlayers([3,4]))
print(dividePlayers([1,1,2,3]))

#Link: https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/