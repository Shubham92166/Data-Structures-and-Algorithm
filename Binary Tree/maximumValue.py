def maximumValue(self,node):
    # code here
    ans = []
    level = 1
    self.recursive(node, level, ans)
    return ans

def recursive(self, root, level, ans):
    if not root:
        return
    if len(ans) < level:
        ans.append(root.data)
    else:
        ans[level-1] = max(ans[level-1], root.data)
    self.recursive(root.left, level+1, ans)
    self.recursive(root.right, level+1, ans)

#Complexity:
#Time: O(N) # N is the total no. of nodes
#Space: O(H) #H is the height of the tree

#Test Cases:
#[1, 2, 3, N, N, 4, 6, N, 5, N, N, 7, N]

#Link: https://practice.geeksforgeeks.org/contest/interview-series-amazon/problems/#
 