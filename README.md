# Benchmark Analysis of Sorting Algorithm <br>
<br>
<br>
The purpose of this project was to find out wich algorithm among BubbleSort, QuickSort, HeapSort and Binary Search Tree was the fastest in sorting a list of *n* random integer with <b>0 < n < 1000</b>, returning the maximum and the minimum integer in the list.<br>
The QuickSort algorithm split a list of length <b>n</b> using a pivot element choosed in the middle of the list, ending up with a <b>logn</b> divisions. In order to find the split point, each of the <b>n</b> items needs to be checked against the pivot value. This result in a <b>nlogn</b> complexity. Trying to avoid the worst case scenario, where the splitting point is very skewed to the left or the right, leaving a very uneven division I used a randomly selected pivot value.<br>
The BubbleSort algorithm compares all the element in a list of lenght <b>n</b> one by one and sort them based on their values. If the first element is greater than the second element, it will swap both the elements moving on to compare the other. This process have to be repeated <b>n-1</b> times regardless of the original arrangement of the list. This generate a O(n<SUP>2</SUP>)complexity
