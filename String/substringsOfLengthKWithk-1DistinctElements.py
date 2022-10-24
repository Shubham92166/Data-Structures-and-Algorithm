def countOfSubstrings(S, K):
    visited = {}
    count = 0
    for i in range(K):
        visited[S[i]] = visited.get(S[i], 0)+1
    
    if len(visited) == K-1:
        count += 1
    
    for i in range(K, len(S)):
        visited[S[i-K]] = visited.get(S[i-K], 0)-1
        if visited.get(S[i-K], 0) == 0:
            del visited[S[i-K]]
        visited[S[i]] = visited.get(S[i], 0) + 1
        if len(visited) == K-1:
            count += 1
    return count

#Complexity:
#Time: O(n)
#Space: O(n)

#Test Cases:
#"abcc", "aabab"

print(countOfSubstrings("abcc", 2)) 
print(countOfSubstrings("aabab", 2))

#Link: https://practice.geeksforgeeks.org/problems/substrings-of-length-k-with-k-1-distinct-elements/1