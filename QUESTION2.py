"""


- Linear search: Linear search,  is a simple search algorithm that looks for a specific element
                in a list or array by checking each element one by one in a sequential
                order until the target element is found or the end of the list is reached.
                Linear search is used for searching and not sorting. It is inefficient for
                large datasets, as it has a time complexity of O(n) in the worst case, where
                'n' is the number of elements.


- Binary Search:Binary search is an efficient search algorithm used for finding a specific element
                in a sorted array. It works by repeatedly dividing the search interval in half until the target element
                is found or determined not to exist. Binary search is a search algorithm and not a sorting algorithm.
                It is particularly efficient for large sorted datasets, witha time complexity of O(log n), where 'n' is the number of elements. However, it relies on a sorted input.


-Merge Sort: Merge sort is a divide-and-conquer sorting algorithm that efficiently sorts a
            list or array by recursively dividing it into smaller sublists, sorting those sublists, and
            then merging them back together. Merge sort is a sorting algorithm, not a searching algorithm.
            It is known for its consistent time complexity of O(n log n) and is used for sorting elements
            into the desired order.

Quick Sort: Quick sort is another efficient sorting algorithm that uses a divide-and-conquer approach.
            It selects a pivot element, partitions the array into two subarrays (elements smaller and larger than
            the pivot), and recursively sorts those subarrays. Quick sort is a sorting algorithm, not a searching
            algorithm. It is known for its average-case time complexity of O(n log n)
            and is widely used for sorting large datasets. However, its worst-case performance can be O(n^2).



"""

def Max(arr):
    if len(arr) == 0:
        return "It is empty"
    
    maxx = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > maxx:
            maxx = arr[i]
    return maxx

arrr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arrr2 = [2]
arrr3 = []

print(Max(arrr2))
print(Max(arrr))
print(Max(arrr3))



"""
THE PSEUDO_CODE OF THE ABOVE CODE IS :

function is Max(arr):
    if the length of the arr is equal to 0:
        then return "empty"
    
    the max_value = arr[0]
    
    for i from 1 to length of arr - 1:
        if the array element arr[i] > max_value:
            max_value = arr[i]
    
    then return max_value





For the Time Complexity:

Here The time complexity is O(n), where 'n' is the number of elements in the input array.
This function iterates through the array once to find the maximum value, and the loop runs 'n-1' times.
In the worst case, the function makes 'n-1' comparisons, which is a linear operation
and we know that linear operation has a big O of O(n).

Space Complexity:

The space complexity of this function is O(1), which means it uses a constant amount
of additional memory that does not depend on the size of the input array.
The function only uses a fixed amount of space to store max_value and the
loop index variable i. The size of the input array does not affect
the amount of memory used.



"""





    
    
