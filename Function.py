import operator
import random

class Function: # will replace with sympy function later

    functions = [operator.add, operator.mul, pow] 

    def __init__(self, index_of_func, arity = 2):
        self.function = self.functions[index_of_func]
        self.arity = arity

    def random_function():
        index = int(random.uniform(0,3))
        return Function(index)

    def arity(self):
        return self.arity

    def __str__(self):
        return "Function: " + str(self.function) + ", arity: " + str(self.arity)



