#time limit exceeded.
# class MedianFinder:

#     def __init__(self):
#         self.list = []
        

#     def addNum(self, num: int) -> None:
#         self.list.append(num)
#         self.list.sort()
        

#     def findMedian(self) -> float:
#         n = len(self.list)
#         if n % 2 == 1:
#             return self.list[n // 2]
#         else:
#             return (self.list[n // 2] + self.list[n // 2 - 1]) / 2
        
import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        if self.left and self.right and -self.left[0] > self.right[0]:
            heapq.heappush(self.right, -heapq.heappop(self.left))

        #make sure that left never longer than right more than 1
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

        
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        else:
            return -self.left[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()