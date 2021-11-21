'''
• Remove one element from an empty BinaryHeap
• Add 3 elements: add(2), add(1), add(5)
• Check that size() returns 3
• Remove one element: remove() and check that it returns 1.
• Add 3 elements: add(4), add(1), add(3).
• Check that size() returns 5
• Remove all the elements and check that they return in order 1,2,3,4,5
'''
import BinaryHeap

q = BinaryHeap.BinaryHeap()

q.remove()
print(q.n)
q.add(2)
q.add(1)
q.add(5)
print(q.size()) # 3 Checked
q.remove()
q.add(4)
q.add(1)
q.add(3)
print(q.size()) # 5 Checked

print(q.a)
for _ in range(q.n):
    r = q.remove()
    print(r)
    print(q.a)
print(q.a)