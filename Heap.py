import heapq


class HeapSort(object):
     
    def __init__(self):
        self.content_min = []
        self.content_max = []
 
    def append(self, value):
        heapq.heappush(self.content_min, value)
        heapq.heappush(self.content_max, -value)
 
    def getMin(self):
        if len(self.content_min) > 0:
            return self.content_min[0]
 
    def getMax(self):
        if len(self.content_max) > 0:
            return -self.content_max[0]
    
    def getClassName(self):
        return "HeapSort"
    
    def clean(self):
        self.content_min = []
        self.content_max = []