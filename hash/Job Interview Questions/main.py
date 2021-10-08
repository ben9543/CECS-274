'''
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
                r.append(i)
                r.append(j)
    return r

    
def two_sum(a, target):
    hash_table = {}
    for i in range(len(a)):
        complement = target - a[i]
        if complement in hash_table:
            return [i, hash_table[complement]]
        hash_table[a[i]] = i
