from SLLStack import SLLStack
from SLLQueue import SLLQueue
from DLList import DLList

'''
Remove one element from an empty Stack, Queue, List
• Stack: Add 5 elements and remove them and check that they are in opposite order
of insertion, e.g., Inserting the sequence 5,4,3,2,1 result in the sequence 1,2,3,4,5 when
removing
• Queue: Add 5 elements and remove them and check that they are in the same order
of insertion, e.g., Inserting the sequence 1,2,3,4,5 result in the sequence 1,2,3,4,5 when
removing
• List: Add 5 elements in different positions (including the first and last) and check that
they are in order, e.g., add(0, 4), add(0, 1), add(1, 3), add(1, 2), and add(4, 5). Then get(i)
should return i + 1. Remove 2 elements, e.g., index 2 and 3 and the final list should be
"1,2,4".

'''

print("Stack: ")
stack = SLLStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nQueue: ")
queue = SLLQueue()
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
queue.add(5)
print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())

print("\nDLList: ")
dllist = DLList()
dllist.add(0, 4)
dllist.add(0, 1)
dllist.add(1, 3)
dllist.add(1, 2)
dllist.add(4, 5)
print(dllist.get(0)) # should return i + 1.
print(dllist.get(1)) # should return i + 1.
print(dllist.get(2)) # should return i + 1.
print(dllist.get(3)) # should return i + 1.
print(dllist.get(4)) # should return i + 1.
dllist.remove(2)
dllist.remove(3)
print(dllist)