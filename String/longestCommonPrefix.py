def longestCommonPrefix(strs):
    prefix = strs[0]
    for str in strs:
        while not str.startswith(prefix):
            prefix = prefix[:-1]
    return prefix

#Test Cases:
#["flower","flow","flight"], ["dog","racecar","car"]

print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["flower","flow","flight"]))