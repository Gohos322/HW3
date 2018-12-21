# Benchmark Analysis of Sorting Algorithm <br>
<br>
<br>
The purpose of this project was to find out wich algorithm among BubbleSort, QuickSort, HeapSort and Binary Search Tree was the fastest in sorting a list of *n* random integer with <b>0 < n < 1000</b>, returning the maximum and the minimum integer in the list.<br>
The QuickSort algorithm split a list of length <b>n</b> using a pivot element choosed in the middle of the list, ending up with a <b>logn</b> divisions. In order to find the split point, each of the <b>n</b> items needs to be checked against the pivot value. This result in a <b>nlogn</b> complexity. Trying to avoid the worst case scenario, where the splitting point is very skewed to the left or the right, leaving a very uneven division I used a randomly selected pivot value.<br>
To return the minimum and the maximum value i just returned the element of index[0] and the element of index[-1] of the sorted list.<br>  
The BubbleSort algorithm compares all the element in a list of lenght <b>n</b> one by one and sort them based on their values. If the first element is greater than the second element, it will swap both the elements moving on to compare the other. This process have to be repeated <b>n-1</b> times regardless of the original arrangement of the list. This generate a <br>O(n<SUP>2</SUP>)</br> complexity. To optimize the algorithm I introduced a flag to monitor whether elements are getting swapped inside the inner for loop. If for a particular iteration, no swapping took place, it means the array has been sorted and we can jump out of the loop, instead of executing all the iterations.<br>
Here again I returned the element of index[0] and the element of index[-1] to get the minimum and maximum value.<br>
To create and sorting the Heap I used the Heap python native library. The class use the same method to generate a maximum Heap, and a maximum Heap with the same element with negative value. To get the minimum element I returned the element of index[0] of the first Heap and for the maximum value, the element of index[0] of the former. <br>
The Binary Search Tree relies on the property that keys that are less than the parent are found in the left subtree, and keys that are greater than the parent are found in the right subtree. This property remains contant for parents and childs. On average a Binary Search tree with <b>n</b> node have <b>O(logn)</b> height and searching requires time proportional to the height of the tree, which is <b>O(logn)</b><br>
To Measure time I originally used time.time(), but I found out that the &Delta; Time measured was on the order of thenths of a second, so i moved to datetime.now(), wich i used to create a function that measure difference of time in the order of milliseconds. I then used pandas to create a DataFrame and stored the result of <br>3</b> repetition in a .cvs <a href="https://github.com/Gohos322/HW3/blob/master/benchmark_data.csv">file</a><br>
<br>
# Performance of Add <br>
<br>
![Add](
        HW3/Performance of Add.png
      )
