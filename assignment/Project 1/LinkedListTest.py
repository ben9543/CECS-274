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

stack = SLLStack()
queue = SLLQueue()
dllist = DLList()