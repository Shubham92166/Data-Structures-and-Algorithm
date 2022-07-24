def makeBeautiful(arr):
    stack = []
    for i in range(len(arr)):
        if not stack:
            stack.append(arr[i])
        else:
            if (arr[i] >= 0 and stack[-1] < 0) or (arr[i] < 0 and stack[-1] >= 0):
                stack.pop()
            else:
                stack.append(arr[i])
    return stack

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#[4,2,-2,1], [2,-2,1,-1], [-3,-1,-19,0,6,-13,12]

print(makeBeautiful([-3,-1,-19,0,6,-13,12]))
print(makeBeautiful([2,-2,1,-1]))
print(makeBeautiful([4,2,-2,1]))
