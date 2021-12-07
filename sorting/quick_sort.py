# Average case time complexity - O(nlog(n))
# Worst case time complexity (when it's sorted) - O(n^2)
# In-place algorithm

# Process:
# 1. Select a pivot
# 2. Move all the elements to the left, that are LESS than pivot
# 3. Move all the elements to the right, that are BIGGER than pivot
# 4. Use recursion to sort each left and right with the same logic
# 5. If the broken down array's length is one, then stop recursion

def quick_sort(a, start, end):
    if start < end:
        pIndex = partition(a,start,end)
        quick_sort(a, start, pIndex-1)
        quick_sort(a, pIndex, end)


# After finishing the for loop, 
# all the elements less than pivot will be on the left
# and all the elements bigger than pivot will be on the right of the pIndex(including pIndex itself)
# Last step: swap pivot and partitioning index element at the last

def partition(a, start, end):
    pivot = a[end]
    pIndex = start
    for i in range(start, end):
        if a[i] <= pivot : 
            a[i], a[pIndex] = a[pIndex], a[i] # swap
            pIndex += 1
    a[pIndex], a[end] = a[end], a[pIndex]
    return pIndex

def prof_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        # Find leftmost element greater than or equal to pivot
        i += 1
        while arr[i] < pivot:
            i += 1
        # Find rightmost element smaller than or equal to pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1
        # If two pointers met
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def prof_quick_sort(arr, low, high):
    if low < high:
        pi = prof_partition(arr, low, high)
        prof_quick_sort(arr, low, pi)
        prof_quick_sort(arr, pi+1, high)

a = [3,4,2,9,5,6,1,7,8,10,12,11]
prof_quick_sort(a, 0, len(a)-1)
print(a)