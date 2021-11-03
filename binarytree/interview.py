'''
Question1: Given the roots of two binary trees, write a function to check if they are the same or not.
'''

def are_tress_identical(t1, t2):
    if t1 == None and t2 == None:
        return True
    if t1 == None or t2 == None:
        return False
    if t1.val != t2.val:
        return False
    return are_tress_identical(t1.right, t2.right) and are_tress_identical(t1.left, t2.left)

'''
Question2: Given a binary search tree, 
find the lowest common ancestor of two given nodes in the BST. The lowest common ancestor is defined between two nodes p and q as the lowest node in a binary tree that has both p and q as descendants.
''' 
def lowest_common_ancestor(root, p, q):
    
    # if p.val and q.val is bigger than root.val
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # if p.val and q.val is smaller than root.val
    elif p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    else: 
        return root
'''
Question3: Given the roots of two binary trees, return true if the second tree is a subtree of the first tree.
* Time complexity: O9mn) where m and n are the number of nodes in the tree and subtree.
'''
def is_subtree(tree, subtree):
    if subtree is None:
        return True
    if tree is None:
        return False
    if are_tress_identical(tree, subtree):
        return True
    return is_subtree(tree.left, subtree) or is_subtree(tree.right, subtree)

'''
Question4: Write a function to merge two binary trees.
'''
def merge_trees(t1, t2):
    if t1 == None:
        return t2
    if t2 == None:
        return t1
    t1.val += t2.val
    t1.left = merge_trees(t1.left, t2.left)
    t1.right = merge_trees(t1.right, t2.right)

'''
Question5: Write a function to convert a given tree to its sum tree
1. Post-order traversal
2. Store the old value of the current node
'''
def to_sum_tree(tree):
    if tree == None:
        return 0
    old_val  = tree.val
    tree.val = to_sum_tree(tree.left) + to_sum_tree(tree.right)
    return tree.val + old_val

'''
Question6: Write a function to check if there exists a subtree in a given binary
tree (r) whose sum of all nodes is equal to a given number (sum)
'''
def sum_subtree_util(ptr, cur_sum, sum):
    pass
