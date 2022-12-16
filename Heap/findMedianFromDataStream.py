from heapq import *
class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap =[]
        self.lengthOfMinHeap = 0
        self.lengthOfMaxHeap = 0
      
        heapify(self.maxHeap)
        heapify(self.minHeap)

    def addNum(self, num):
        heappush(self.maxHeap, -num)
        self.lengthOfMaxHeap += 1
        
        heappush(self.minHeap, self.popMax(self.maxHeap))
        
        self.lengthOfMaxHeap -= 1
        self.lengthOfMinHeap += 1
        
        
        if self.lengthOfMinHeap > self.lengthOfMaxHeap:
            heappush(self.maxHeap, -self.popMin(self.minHeap))
            
            self.lengthOfMaxHeap += 1
            self.lengthOfMinHeap -= 1
    

    def findMedian(self):
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        
        else:
            return (-self.maxHeap[0] + self.minHeap[0])/2
         
    def popMin(self, heap):
        return heappop(heap)
    
    def popMax(self, heap):
        return -1*heappop(heap)
    
#Complexity:
#Time: Add operation: O(log n) and find operation O(1)
#Space: O(n)
#Where n is the size of the data stream

#Test Cases:
#["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"], [[], [1], [2], [], [3], []]

#Link: https://leetcode.com/problems/find-median-from-data-stream/