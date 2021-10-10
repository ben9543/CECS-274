from SLLStack import SLLStack
from SLLQueue import SLLQueue
from DLList import DLList
from MaxStack import MaxStack

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

# isPalindrome() test
# Question: the element at position i is equal to the element at position n − i − 1 
dllist = DLList()

# With 'a'
dllist.add(0, 'a')
print(dllist.isPalindrome())

# With 'hannah'
dllist = DLList()
dllist.add(0, 'h')
dllist.add(1, 'a')
dllist.add(2, 'n')
dllist.add(3, 'n')
dllist.add(4, 'a')
dllist.add(5, 'h')
print(dllist.isPalindrome())

# With 'eve'
dllist = DLList()
dllist.add(0, 'e')
dllist.add(1, 'v')
dllist.add(2, 'e')
print(dllist.isPalindrome())

# With a word that is not palindrome
dllist = DLList()
dllist.add(0, 'e')
dllist.add(1, 'v')
dllist.add(2, 'a')
dllist.add(3, 'v')
dllist.add(4, 'a')
print(dllist.isPalindrome())

# Reverse
dllist = DLList()
dllist.add(0, 1)
dllist.add(1, 2)
dllist.add(2, 3)
dllist.add(3, 4)
dllist.add(4, 5)
# dllist.reverse()

# 4. MaxStack
m = MaxStack()
m.push(3)
m.push(1)
m.push(4)
m.push(2)
print(m.max())
m.pop()
m.pop()
print(m.max())
m.pop()
print(m.max())
# print(m.size())