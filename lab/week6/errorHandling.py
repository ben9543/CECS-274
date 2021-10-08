# Singly LL
# Doubly LL
# Circular LL

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        #self.tail = None
        #self.n = 0
    def append(self, data):
        new = Node(data)
        if(self.head == None):self.head = new
        else:
            cur = self.head
            while(cur.next!=None): cur = cur.next
            cur.next = new
            #self.tail = cur
    def printList(self):
        cur = self.head
        while(cur!=None): 
            print(cur.data)
            cur = cur.next
    def insert(self, position, data):
        new = Node(data)
        if position == 0: 
            new.next = self.head
            self.head = new
        cur = self.head
        prev = None
        while(position > 0):
            prev = cur
            cur = cur.next 
            position-=1
        prev.next = new
        new.next = cur
        return

    def reverse(self):
        p = None
        q = self.head
        r = None
        while(q != None):
            
            # Move next pointer
            r = q.next
            
            # Point q.next to previous node
            q.next = p

            # Move previous node to current node
            p = q

            # Update current node to the next node. 
            # Since q.next no points the previous node, we have to use r to move on to the next node.
            q = r

        # Head node points to previous node (when the loop ends, q is None. p is the last node)
        self.head = p
    
    def getMiddleElement(self):
        fast = self.head
        slow = self.head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow.data

l = LinkedList()

# Append
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
# l.append(6)

# GetMiddleElement test
print(f"Middle el: {l.getMiddleElement()}")

# Revese test
l.reverse()
l.printList()
