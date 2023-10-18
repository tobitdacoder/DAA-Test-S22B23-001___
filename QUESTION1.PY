
def swap(arr, i, j): # This swap function takes an array arr and two indices i and j,
                    #and it swaps the elements at those indices. This allows you to swap elements in the insertionSort function as needed to sort the array.
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def insertionSort(Arr,n):
    for pos in range(1,n):
        nextpos=pos
        while nextpos > 0 and Arr[nextpos] < Arr[nextpos -1]:
            swap(Arr,nextpos,nextpos-1)
            nextpos=nextpos-1
    return Arr


UnList = [53, 22, 19, 39, 16, 14, 88]

SList= insertionSort(UnList, len(UnList))

print(SList)




"""
2. ANALYSIS:

The working principle of the Insertion sort is that, it builds a sorted section of an array
by inserting each unsorted element into its correct position within the sorted section.
This process is repeated until the entire array is sorted. The time complexity of the
insertion sort is O(n^2), this is in the worst and average cases, then O(n) in the best
case for arrays which are almost sorted.

So we can now tell that  the nest case scenario occurs when the array is almost or nearly sorted.

3. TESTING

Yes the list was sorted!!!!.

4. COMPARISON:

Comparing to Bubble sort and Merge sort, insertion Sort is Simple, efficient, But only
for small datasets and almost sorted data. in its best-case scenario, it has O(n), In its
worst-case O(n^2).

When it comes to the bubble Sort, This is also Simple but the catch is that it is
less efficient than insertion sort. However, they both have almost equal use cases,
but This is ess preferred.

For merge Sort, This one is THE BEST, because it is efficient for bigger or larger datasets.
It has a consistent time complexity of O(n log n) .This makes it  Ideal for general
sorting tasks,However it uses extra memory.

5. PRACTICAL SCENARIO:


In the case that we have  a nearly sorted list with just a few elements out of order. then
Yes, The insertion sort is a pretty good choice. That is because it has a best-case time
complexity of O(n) in such situations, making it efficient for this specific use case. So
It will only need to pass through the array for a few times (depending on the length of the small list)






"""
            
