
'''
We have 3 steps
1, 2, 3
How many ways are possible that we can compelete n stairs using 1,2,3?
'''
def countWays(n):
    if n == 0:
        return 1
    elif n == 1 or n == 2:
        return n
    else:
        return countWays(n-3) + countWays(n-2) + countWays(n-1)

'''
def completeCountWays(n):
    res = [0] * (n-2)

    for i = in range(3, n+1):
        res[i] = res[i-3] + res[i-2] + res[i-1]
'''

'''
# QuickSort
Divide and Conquer

Choose a "pivot" and divide the array into 2 halves where 
the left half is less than (or equal to the pivot and the right half is greater than the pivot.
'''

def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if(start < end):
            # swap
            array[start], array[end] = array[end], array[start]
        
