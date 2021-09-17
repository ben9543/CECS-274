class Stack:
    pass

class SSList(Stack):
    class Node:
        def __init__(self, x):
            self.next = None
            self.x = x
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.n = 0

    def pop(self):
        if self.n == 0: return None
        x = self.head.x
        self.head = self.head.next
        self.n -= 1
        if self.n == 0: self.tail = None
        return x

    def add(self, x):
        u = self.Node(x)
        if self.n == 0:self.head = u
        else:self.tail.next = u
        self.tail = u
        self.n += 1
        return True
class DLList(Stack):
    class Node:
        def __init__(self, x):
            self.next = None
            self.x = x
    def __init__(self):
        self.n = 0
        self.dummy = self.Node(None)
        self.prev = self.dummy
        self.next = self.dummy

    def get(self, i):
        return self.get_node(i).x

    def set(self, i, x):
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def add(self, i, x):
        return self.add_before(self.get_node(i), x)

    def get_node(self, i):
        if i < self.n/2:
            p = self.dummy.next
            for k in range(0,i):
                p = p.next
        else:
            p = self.dummy.prev
            for k in range(0,i):
                p = p.prev

    def add_before(self, w, x):
        u = self.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u # w.prev
        u.next.next = u # w.next
        self.n += 1
        return u

        