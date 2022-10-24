def firstBadVersion(n):
    l, r=1,n
    while(l<=r):
        mid=(l+r)//2

        #isBadVersion method is implemented by the Leetcode 

        if(isBadVersion(mid)==True):
            r= mid-1
        else:
            l=mid+1
    return l

#Test Cases: 
#5, 4
#2126753390, 1702766719
#1, 1

#Complexity:
#Time: O(log n)
#Space: O(1)

#Link: https://leetcode.com/problems/first-bad-version/
