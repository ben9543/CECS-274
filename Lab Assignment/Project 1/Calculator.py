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
        pass

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