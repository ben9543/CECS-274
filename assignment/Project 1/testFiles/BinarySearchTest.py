from BinarySearchTree import BinarySearchTree
q = BinarySearchTree()

# Need to do add function
q.add(2, "second")
q.add(1, "first")
q.add(3, "third")
q.add(5, "fifth")
q.add(4, "fourth")

print("Root: " + q.r.v)

'''
q.in_order()
print()
q.pre_order()
print()
q.post_order()
'''
'''
print(q.find(2.5))
print()
q.remove(3)
q.pre_order()
print()
print(q.find(3))
print(q.find_eq(3.4))
print(q.find_eq(3))
print(q.find_eq(4).v)
q.bf_traverse()
'''

'''
q.add(3, "third")
q.add(5, "fifth")
q.add(4, "fourth")
'''

'''
print(q.find_eq(3.4))
print(q.find(3.4))
print("In order")
q.in_order()
print("Pre oder")
q.pre_order()
print("Pos order")
q.post_order()
'''
