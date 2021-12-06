# Worst case time complexity - O(nlog(n))   
# Space complexity - O(n) (not in-place)
def merge_sort(a):
    # Take the length of array and divide it by two
    if (len(a) < 2):
        return a
    m = len(a)//2
    a0 = merge_sort(a[:m])
    a1 = merge_sort(a[m:len(a)])
    merge(a0, a1, a)
    return a

def merge(a0, a1, a):
    i = j = k = 0
    l0 = len(a0)
    l1 = len(a1)
    while i < l0 and j < l1:
        if a0[i] <= a1[j]:
            a[k] = a0[i]
            i += 1
        else:
            a[k] = a1[j]
            j += 1
        k += 1
    while i < l0:
        a[k] = a0[i]
        i += 1
        k += 1
    while j < l1:
        a[k] = a1[j]
        j += 1
        k += 1
a = [3,4,2,9,5,6,1,7,8,10]
print(merge_sort(a))