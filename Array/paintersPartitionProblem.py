def paint(A, B, C):
    l, r = max(C), sum(C)*B
    while l <= r:
        mid = l+(r-l)//2
        if not is_Valid(C, A, B, mid):
            l = mid+1
        else:
            r = mid-1
    return (l) % 10000003

def is_Valid(boats, paintersCount, time_per_boat, expected_time):
    n = len(boats)
    i = 0
    while paintersCount > 0:
        time = 0
        while i < n and time + boats[i]*time_per_boat <= expected_time:
            time += boats[i]*time_per_boat
            i += 1
        if i == n:
            return True
        paintersCount -= 1
    return False 

#Complexity:
#Time: O(nlogn)
#Space: O(1)

#Test Cases:
#2, 5, [1, 10]
#10, 1, [1, 8, 11, 3]

print(paint(10, 1, [1, 8, 11, 3]))
print(paint(2, 5, [1, 10])) 
