def canConstruct(ransomNote, magazine):
        dic1 = {}
        dic2 = {}

        if len(magazine) < len(ransomNote):
            return False

        for i in ransomNote:
            dic1[i] = dic1.get(i, 0) + 1
            
        for i in magazine:
            dic2[i] = dic2.get(i, 0) + 1
            
        for i in ransomNote:
            count = dic1.get(i)
            if dic2.get(i, -1) < count:
                return False

        return True

#Complexity:
#Time: O(m)
#Space: O(m)
#where m is the length of magazine

#Test Cases:
#"a", "b"
#"aa", "ab"
#"aa", "aab"
#"bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
print(canConstruct("bg", "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))

#Link: https://leetcode.com/problems/ransom-note/