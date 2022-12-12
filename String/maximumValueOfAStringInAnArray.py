def maximumValue(strs):
    maxVal = 0
    
    for st in strs:
        if st.isnumeric():
            maxVal = max(int(st), maxVal)
        else:
            maxVal = max(maxVal, len(st))
    
    return maxVal

#Complexity:
#Time: O(n^2)
#Space: O(1)
#Where n is the length of the string

#Test Cases:
#["alic3","bob","3","4","00000"], ["1","01","001","0001"]

print(maximumValue(["alic3","bob","3","4","00000"]))
print(maximumValue(["1","01","001","0001"]))

#Link: https://www.geeksforgeeks.org/python-string-isnumeric-method/