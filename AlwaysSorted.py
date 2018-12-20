import random, time, heapq
from BinarySearchTreeClass import BinarySearchTree
from BubbleSort import BubbleSort
from Heap import HeapSort
from QuickSort import QuickSort
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta

def measure_time(a, this_list):
    tot_time_add = 0
    tot_time_min = 0
    tot_time_max = 0
 
    for num in this_list:
        start = datetime.now()
        a.append(num)
        tot_time_add += millis(start)
 
        start = datetime.now()
        a.getMin()
        tot_time_min += millis(start)
 
        start = datetime.now()
        a.getMax()
        tot_time_max += millis(start)
 
    return tot_time_add, tot_time_min, tot_time_max

def millis(start_time):
    dt = datetime.now() - start_time
    ms = (dt.days * 24 * 3600 + dt.seconds) * 1000 + dt.microseconds / 1000.0
    return ms

def elabora(a, this_list, rounds, repetitions):

    tot_time_add, tot_time_min, tot_time_max = 0, 0, 0
    for _ in range(repetitions):
        a.clean()
        myadd, mymin, mymax = measure_time(a, this_list)
        tot_time_add += myadd
        tot_time_min += mymin
        tot_time_max += mymax

    tot_time_add /= repetitions
    tot_time_min /= repetitions
    tot_time_max /= repetitions

    return tot_time_add, tot_time_min, tot_time_max

 
if __name__ == '__main__' : 
    repetitions = 3
    max_operations = 800
    step = 200
 
    values_quickbubble_add, values_quickbubble_min, values_quickbubble_max = [], [], []
    values_quicksort_add, values_quicksort_min, values_quicksort_max = [], [], []
    values_heap_add, values_heap_min, values_heap_max = [], [], []
    values_bubble_add, values_bubble_min, values_bubble_max = [], [], []
    values_binarytree_add, values_binarytree_min, values_binarytree_max = [], [], []

    for rounds in range(step, max_operations, step):
        this_list = []
        for r in range(rounds):
            this_list.append(random.randint(0,1000))

        values_add, values_min, values_max = elabora(BubbleSort(True), this_list, rounds, repetitions)
        print("BubbleSort(True) done!")
        values_quickbubble_add.append(values_add)
        values_quickbubble_min.append(values_min)
        values_quickbubble_max.append(values_max)
        values_add, values_min, values_max = elabora(BubbleSort(False), this_list, rounds, repetitions)
        print("BubbleSort(False) done!")
        values_bubble_add.append(values_add)
        values_bubble_min.append(values_min)
        values_bubble_max.append(values_max)
        values_add, values_min, values_max = elabora(QuickSort(), this_list, rounds, repetitions)
        print("QuickSort() done!")
        values_quicksort_add.append(values_add)
        values_quicksort_min.append(values_min)
        values_quicksort_max.append(values_max)
        values_add, values_min, values_max = elabora(BinarySearchTree(), this_list, rounds, repetitions)
        print("BinarySearchTree() done!")
        values_binarytree_add.append(values_add)
        values_binarytree_min.append(values_min)
        values_binarytree_max.append(values_max)        
        values_add, values_min, values_max = elabora(HeapSort(), this_list, rounds, repetitions)
        print("HeapSort() done!")
        values_heap_add.append(values_add)
        values_heap_min.append(values_min)
        values_heap_max.append(values_max)
    
    data=np.array([values_quickbubble_add, values_quickbubble_min, values_quickbubble_max])
    df=pd.DataFrame(data=data[0:,0:], index=["add", "min", "max"], columns=["QuickBubbleSort"]*len(values_quickbubble_add)).transpose()
    data= np.array([values_bubble_add, values_bubble_min, values_bubble_max])
    df2=pd.DataFrame(data=data[0:,0:], index=[ "add", "min", "max"], columns=["BubbleSort"]*len(values_bubble_add)).transpose()
    df=df.append(df2)
    data= np.array([values_quicksort_add, values_quicksort_min, values_quicksort_max])
    df2=pd.DataFrame(data=data[0:,0:], index=[ "add", "min", "max"], columns=["QuickSort"]*len(values_quicksort_add)).transpose()
    df=df.append(df2)
    data= np.array([values_heap_add, values_heap_min, values_heap_max])
    df2=pd.DataFrame(data=data[0:,0:], index=[ "add", "min", "max"], columns=["HeapSort"]*len(values_heap_add)).transpose()
    df=df.append(df2)
    data= np.array([values_binarytree_add, values_binarytree_min, values_binarytree_max])
    df2=pd.DataFrame(data=data[0:,0:], index=[ "add", "min", "max"], columns=["BinaryTree"]*len(values_binarytree_add)).transpose()
    df=df.append(df2)


    xlabels = range(step, max_operations, step)
 
    plt.plot(xlabels, values_quickbubble_add, label='Add')
    plt.plot(xlabels, values_quickbubble_min, label='Get Min')
    plt.plot(xlabels, values_quickbubble_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of List Elements")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of QuickBubbleSort Solution")
    plt.show()
 
    plt.plot(xlabels, values_bubble_add, label='Add')
    plt.plot(xlabels, values_bubble_min, label='Get Min')
    plt.plot(xlabels, values_bubble_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of List Elements")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of BubbleSort Solution")
    plt.show()
 
    plt.plot(xlabels, values_quicksort_add, label='Add')
    plt.plot(xlabels, values_quicksort_min, label='Get Min')
    plt.plot(xlabels, values_quicksort_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of List Elements")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of QuickSort Solution")
    plt.show()
 
    plt.plot(xlabels, values_heap_add, label='Add')
    plt.plot(xlabels, values_heap_min, label='Get Min')
    plt.plot(xlabels, values_heap_max, label='Get Max')
    plt.legend()
    plt.xlabel("Number of List Elements")
    plt.ylabel("Execution time (msec)")
    plt.title("Performance of Heap Solution")
    plt.show()
 
    plt.plot(xlabels, values_binarytree_add, color='b', linestyle='-', label='Add')
    plt.plot(xlabels, values_binarytree_min, color='b', linestyle='--', label='Get Min')
    plt.plot(xlabels, values_binarytree_max, color='b', linestyle='-.', label='Get Max')
    plt.legend()
    plt.xlabel("Number of List Elements")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of BinaryTree Sort")
    plt.show()
 
    plt.plot(xlabels, values_quickbubble_add, color='g', linestyle='-', label='QuickBubbleSort Add')
    plt.plot(xlabels, values_bubble_add, color='r', linestyle='-', label='BubbleSort Add')
    plt.plot(xlabels, values_quicksort_add, color='b', linestyle='-', label='QuickSort Add')
    plt.plot(xlabels, values_heap_add, color='y', linestyle='-', label='Heap Add')
    plt.plot(xlabels, values_binarytree_add, color='c', linestyle='-', label='BinaryTree Add')
    plt.legend()
    plt.xlabel("Number of List Elements")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Add")
    plt.show()
 
    plt.plot(xlabels, values_quickbubble_min, color='g', linestyle='-', label='QuickBubbleSort Min')
    plt.plot(xlabels, values_bubble_min, color='r', linestyle='-', label='BubbleSort Min')
    plt.plot(xlabels, values_quicksort_min, color='b', linestyle='-', label='QuickSort Min')
    plt.plot(xlabels, values_heap_min, color='y', linestyle='-', label='Heap Min')
    plt.plot(xlabels, values_binarytree_min, color='c', linestyle='-', label='BinaryTree Min')
    plt.legend()
    plt.xlabel("Number of List Elements")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Get Min")
    plt.show()
 
    plt.plot(xlabels, values_quickbubble_max, color='g', linestyle='-', label='QuickBubbleSort Max')
    plt.plot(xlabels, values_bubble_max, color='r', linestyle='-', label='BubbleSort Max')
    plt.plot(xlabels, values_quicksort_max, color='b', linestyle='-', label='QuickSort Max')
    plt.plot(xlabels, values_heap_max, color='y', linestyle='-', label='Heap Max')
    plt.plot(xlabels, values_binarytree_max, color='c', linestyle='-', label='BinaryTree Max')
    plt.legend()
    plt.xlabel("Number of List Elements")
    plt.ylabel("Total Execution time (msec)")
    plt.title("Performance of Get Max")
    plt.show()