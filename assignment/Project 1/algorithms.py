"""Implementations of some sorting"""
import random


def merge(a0, a1, a):
    pass

def merge_sort(a):
    pass

def _quick_sort(a, i, n):
    pass

def quick_sort(a):
    _quick_sort(a, 0, len(a))
    

# Assuming that you have an already sorted array
# You can use binary search algorithm to lookup a key in O(log(n)) time
def binary_search(a, n, x) :
    low = 0
    high = n
    mid = 0
    while True:
        if high < low: return -1
        mid = (high + low) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            high = mid - 1
        else:
            low = mid + 1


# arr = [1,2,3,4,5,6,7,8,9,10]
# print(binary_search(arr, len(arr), 7))