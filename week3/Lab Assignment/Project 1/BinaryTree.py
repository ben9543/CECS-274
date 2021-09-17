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
        pass

    def size(self) -> int:
        pass
    
    def _size(self, u : Node) -> int:
        if u == self.nil: return 0
        return 1 + self._size(u.left) + self._size(u.right)
    
    def size2(self) -> int:
        pass

    def height(self) -> int:
        pass
    
    def _height(self, u : Node) -> int:
        if u == self.nil: return 0
        return 1 + max(self._height(u.left), self._height(u.right))
    
    def traverse(self, u : Node):
        pass

    def traverse2(self):
        pass

    def bf_traverse(self):
        pass
            
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
        pass

    def pre_order(self) :
        pass

    def post_order(self) :
        pass

    def __str__(self):
        l = []
        #self.in_order(self.r, l)
        return ', '.join(map(str, l))