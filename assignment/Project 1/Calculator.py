import numpy as np
import ArrayStack
import ChainedHashTable
import DLList
import BinaryTree
import operator

class Calculator:
    def __init__(self) :
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k :str, v : float) :
        self.dict.add(k,v)

    def print_expression(self, s : str) -> str :
        t = ''
        return t

    def matched_expression(self, s : str) -> bool :
<<<<<<< HEAD:Lab Assignment/Project 1/Calculator.py
        stack = list()
        for c in s:
            if c=="(":
                stack.append(c)
            elif c==")":
                stack.pop()
        if stack is None: return True
        else return False
=======
        stack = ArrayStack.ArrayStack()
        try:
            for c in s:
                if c == "(": stack.push(c)
                if c == ")": stack.pop()
            if stack.n == 0: return True
            return False
        except IndexError:
            return False
>>>>>>> e07ae2437cad4c35d01277c5a29a7602e0113037:assignment/Project 1/Calculator.py

    def build_parse_tree(self, exp : str) -> str:
        pass
        

    def _evaluate(self, u):
        pass

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