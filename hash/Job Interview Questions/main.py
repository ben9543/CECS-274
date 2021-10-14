'''
Question 1:
You are given an array of integers and a target integer value,  
return the indices of the two numbers in the array such that they add up to target. 
If no such two numbers exist return an empty result set

a=[1,2,5,7,9,23,3], target=12

[2,3]
'''


def two_sum_OG(a, target):
    r = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if i + j == target:
                return [i, j]
    return r

    
def two_sum(a, target):
    hash_table = {}
    for i in range(len(a)):
        complement = target - a[i]
        if complement in hash_table:
            return [i, hash_table[complement]]
        hash_table[a[i]] = i


'''
Question 2:
Given two Linked Lists, find the intersection of the two lists 
(elements present in both lists)
'''

def findIntersection():
    pass

'''
Question3:
Given an array arr[0..n-1] of distinct integers and a range [low, high], find all numbers t
in that range which do not exist in the array. Print the missing elements in sorted order.
'''

'''
Question4:
Detect if a given linked list has a cycle or not using a hashtable?
'''
def find_missing_numbers(arr, n, low, high):
    nums_hashset =set(arr)
    for i in range(low, high + 1):
        if i not in nums_hashset:
            print(x, end = ' ')
