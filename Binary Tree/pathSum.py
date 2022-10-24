def hasPathSum(root, targetSum):
    if not root:
        return False
    return checkPath(root, 0, targetSum)

def checkPath(root, sum, targetSum):
    if not root:
        return False
    sum += root.val
    if not root.left and not root.right:
        if sum == targetSum:
            return True

        sum -= root.val
        return False

    leftCheck = checkPath(root.left, sum, targetSum)
    rightCheck = checkPath(root.right, sum, targetSum)

    return leftCheck or rightCheck

#Complexity:
#Time: O(n)
#Space: O(h)
#where O(h) can be O(n) in worst case. h is the height and n is the no. of nodes

#Test Cases:
#[5,4,8,11,null,13,4,7,2,null,null,null,1], 22
#[1,2,3], 5

#Link: https://leetcode.com/problems/path-sum/