def maxArea(height):
    i = 0
    water = 0
    j = len(height)-1
    while(i < j):
        water = max(water, (j-i)*(min(height[i], height[j])))
        if height[i] < height[j]:
            i += 1
        else: 
            j -= 1
    return water

#Complexity:
#Time: O(n)
#Space: O(1)

#Test Cases:
#[1,8,6,2,5,4,8,3,7], [1,1]

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))