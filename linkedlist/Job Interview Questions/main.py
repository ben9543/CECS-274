'''
#1 Given the head of a linkedList, delete the n-th node from the End of the list.
'''
def removeNthFromEnd(head:object, n:int):
    '''
    The first pointer moves to location n+1 from the beginning initially,
    while the second pointer starts from the beginning. This way, the two pointers are n nodes apart.
    '''
    firstPtr = head
    secondPtr = head
    for _ in range(n+1):
        firstPtr = firstPtr.next
    # Move both pointers together one step at a time until the first pointer reaches the end
    while firstPtr is not None:
        firstPtr = firstPtr.next
        secondPtr = secondPtr.next
    secondPtr.next = secondPtr.next.next
'''
Question2: Given the head of a linked list, determine if the linked list has a cycle in it or not?
'''
def hasCycle(head: ListNode) -> bool:
    if head is None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True