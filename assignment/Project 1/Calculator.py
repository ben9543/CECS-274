import numpy as np
import ArrayStack
import ChainedHashTable
import DLList
import BinaryTree
import operator

operators = ['+', '-', '*', '/']

class Calculator:
    def __init__(self) :
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)

    def print_expression(self, s : str) -> str :
        t = ""
        if not self.matched_expression(s): return "Invalid expression"
        for c in s:
            if self.dict.find(c):
                t+=str(self.dict.find(c))
            else: t+=c
        return t

    def matched_expression(self, s : str) -> bool :
        stack = ArrayStack.ArrayStack()
        try:
            for c in s:
                if c == "(": stack.push(c)
                if c == ")": stack.pop()
            if stack.n == 0: return True
            return False
        except IndexError:
            return False

    # In Progress
    def build_parse_tree(self, exp : str) -> str:
        stack = []
        t = BinaryTree.BinaryTree()
        
        def isOperator(c):
            if c not in operators: return False
            return True

        for c in exp:
            u = BinaryTree.BinaryTree.Node(c)
            if not isOperator(c):
                stack.append(u)
            else:
                t1 = stack.pop()
                t2 = stack.pop()
                u.left = t1
                u.right = t2
                stack.append(u)
        t.r = stack.pop()
        return t

    def _evaluate(self, u):
        
        if u is None:
            return 0
        if u.left is None and u.right is None:
            return int(u.x)
        left_sum = self._evaluate(u.left)
        right_sum = self._evaluate(u.right)
        
        if u.x == '+':
            return operator.add(left_sum, right_sum)
        elif u.x == '-':
            return operator.sub(left_sum, right_sum)
        elif u.x =='*':
            return operator.mul(left_sum, right_sum)
        else:
            return operator.floordiv(left_sum, right_sum)

    def evaluate(self, exp):
        try:
            parseTree = self.build_parse_tree(exp)
            return self._evaluate(parseTree.r)
        except:
            return 0

'''
s = Calculator()
print(s.evaluate("((a*b)+(c*d))"))
s.set_variable("a", 1.3)
s.set_variable("b", 2.1)
s.set_variable("c", 2.2)
s.set_variable("d", 3.0)
print(s.evaluate("((a*b)+(c*d))"))
'''

# print_expression
'''
s = Calculator()
s.set_variable("a", 1.3)
s.set_variable("b", 2.1)
s.set_variable("c", 2.2)
s.set_variable("d", 3.0)
r = s.print_expression("((a ∗ b) + (c ∗ d))")
print(r)
'''