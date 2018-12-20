from random import randrange
import random

class QuickSort:

    def __init__(self):
        self.content=[]   
    
    def append (self, value):
        self.content.append(value)
        self._quick_sort()

    def _partition(self, lst, start, end, pivot):
        lst[pivot], lst[end] = lst[end], lst[pivot]
        store_index = start
        for i in range(start, end):
            if lst[i] < lst[end]:
                lst[i], lst[store_index] = lst[store_index], lst[i]
                store_index += 1
        lst[store_index], lst[end] = lst[end], lst[store_index]
        return store_index


    def _quick_sort(self):
        lst=self.content
        start=0
        end=len(lst)-1
        self._sort(lst, start, end)

    def _sort(self, lst, start, end):
        if start >= end:
            return lst
        pivot = randrange(start, end + 1)
        new_pivot = self._partition(lst, start, end, pivot)
        self._sort(lst, start, new_pivot - 1)
        self._sort(lst, new_pivot + 1, end)
    
    def getMin(self):
        return self.content[0]
    
    def getMax(self):
        return self.content[-1]

    def getClassName(self):
        return "QuickSort"

    def clean(self):
        self.content=[]         