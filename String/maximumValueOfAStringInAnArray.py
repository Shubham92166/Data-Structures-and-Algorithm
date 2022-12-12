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

#Link: https://www.geeksforgeeks.org/python-string-isnumeric-method/