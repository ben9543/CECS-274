"""Implementations of some sorting"""
import random


def merge(a0, a1, a):
    i = j = curr = 0
    l0 = len(a0)
    l1 = len(a1)
    while i < l0 and j < l1:

        # Compare left and right array and put the smallest one.
        if a0[i] <= a1[j]:
            a[curr] = a0[i]
            i += 1
        else:
            a[curr] = a1[j]
            j += 1
        curr += 1
    
    # Put all remained elements from either left or right element
    while i < l0:
        a[curr] = a0[i]
        i += 1
        curr += 1
    while j < l1:
        a[curr] = a1[j]
        j += 1
        curr += 1

def merge_sort(a):
    # Base Case
    if len(a) <= 1: return a
    mid = len(a) // 2

    # Partitioning
    a0 = merge_sort(a[0:mid])
    a1 = merge_sort(a[mid:len(a)])

    # Merge
    merge(a0, a1, a)
    return a

def _quick_sort(a, i, n):
    if i < n:
        pi = _partition(a, i, n)
        _quick_sort(a, i, pi)
        _quick_sort(a, pi+1, n)

def _partition(arr, low, high):
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

def quick_sort(a):
    if len(a) <= 1: return a
    _quick_sort(a, 0, len(a)-1)
    

# Assuming that you have an already sorted array
# You can use binary search algorithm to lookup a key in O(log(n)) time
def binary_search(a, n, x) :
    low = 0
    high = n
    mid = 0
    
    while True:
        if high < low: return mid
        mid = (high + low) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            high = mid - 1
        else:
            low = mid + 1


# arr = [1,2,3,4,5,6,7,8,9,10]
# arr = [5,4,7,8,9,1,3]
# print(binary_search(arr, len(arr), 7))
# quick_sort(arr)
# print(arr)