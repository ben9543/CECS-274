import ArrayQueue
#from drawtree import draw_bst

class BinaryTree:
    class Node:
        def __init__(self, x : object, v = None) :
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_val(self, x) :
            self.x = x

        def insert_left(self) :
            self.left = BinaryTree.Node('') 
            self.left.parent = self
            return self.left

        def insert_right(self) :
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

    def __init__(self) : 
        self.r = None
        self.nil = None

    def depth(self, u : Node) -> int:
        d = 0
        while True:
            u = u.parent
            d += 1
            if u!=self.r : break
        return d

    def size(self) -> int:
        if self.u == self.nil: return 0
        return 1 + self._size(self.u.left) + self._size(self.u.right)
    
    def _size(self, u : Node) -> int:
        if u == self.nil: return 0
        return 1 + self._size(u.left) + self._size(u.right)
    
    def size2(self) -> int:
        pass

    def height(self) -> int:
        if self.u==self.nil:return 0
        return 1+max(self.height(self.u.left), self.height(self.u.right))

    
    def _height(self, u : Node) -> int:
        if u == self.nil: return 0
        return 1 + max(self._height(u.left), self._height(u.right))
    
    def traverse(self, u : Node):
        pass

    def traverse2(self):
        pass

    def bf_traverse(self):
        q = ArrayQueue.ArrayQueue()
        if self.r != self.nil : q.add(self.r)
        while True:
            self.u = q.remove()
            if self.u.left != self.nil : q.add(self.u.left)
            if self.u.right != self.nil : q.add(self.u.right)
            if q.size() > 0: break
            
    def first_node(self):
        w = self.r
        if w == self.nil: return self.nil
        while w.left != self.nil:
            w = w.left
        return w
    
    def next_node(self, w):
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w
    
    def in_order(self) :
        if self.u.left != self.nil: self.in_order(self.u.left)
        print(self.u.x)
        if self.u.right != self.nil: self.in_order(self.u.right)

    def pre_order(self) :
        print(self.u.x)
        if self.u.left != self.nil: self.in_order(self.u.left)
        if self.u.right != self.nil: self.in_order(self.u.right)

    def post_order(self) :
        if self.u.left != self.nil: self.in_order(self.u.left)
        if self.u.right != self.nil: self.in_order(self.u.right)
        print(self.u.x)

    def __str__(self):
        l = []
        #self.in_order(self.r, l)
        return ', '.join(map(str, l))