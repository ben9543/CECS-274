from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self, nil=None):
        super().__init__()
        self.n = 0
        self.nil = nil
        
    def clear(self):
        self.r = self.nil
        self.n = 0

    # Changed the parameter to accept value. Is it okay??
    def new_node(self, x, value):
        u = BinaryTree.Node(x, value)
        u.left = u.right = u.parent = self.nil
        return u
    
    # x is just value
    def find_last(self, x : object) -> BinaryTree.Node:
        w = self.r
        prev = self.nil
        try:
            while w != self.nil:
                prev = w
                if x < w.x:
                    w = w.left
                elif x > w.x:
                    w = w.right
                else:
                    return w
        except:
            pass

        return prev
    
    # inserting u as p's child
    def add_child(self, p : BinaryTree.Node, u : BinaryTree.Node) -> bool:
        if p == self.nil:
            self.r = u # inserting into empty tree
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False # u.x is already in the tree
            u.parent = p
        self.n += 1
        return True


    def find_eq(self, x : object) -> object:
        w = self.r
        while w is not self.nil:
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return self.nil

    def find(self, x: object) -> object:
        w = self.r
        z = self.nil
        while w is not self.nil:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.v
        if z == self.nil: return self.nil
        return z.v
    
    # Question: What is key and value
    def add(self, key : object, value : object) -> bool:
        p = self.find_last(key)
        return self.add_child(p, self.new_node(key, value))
        
    def add_node(self, u : BinaryTree.Node) -> bool:
        pass
    
    def splice(self, u: BinaryTree.Node):
        s = None
        p = None
        if u.left is not self.nil: s = u.left
        else: s = u.right

        # Handling when u is a root node
        if u == self.r:
            self.r = s
            p = self.nil
        else:
            p = u.parent
            if p.left == u: p.left = s
            else: p.right = s
        if s is not self.nil: s.parent = p
        self.n -= 1

    def remove_node(self, u : BinaryTree.Node):
        if u.left == self.nil or u.right == self.nil:
            self.splice(u)
        else:
            w = u.right
            while w.left == self.nil:
                w = w.left
            u.x = w.x
            self.splice(w)
    
    def remove(self, x : object) -> bool:
        u = self.find_eq(x)
        if u == self.nil: return False
        self.remove_node(u)
        return True
             
    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)