
from operator import add, mul
from random import uniform

class Function(object): # will replace with sympy function later

    functions = [add, mul, pow] 

    def __init__(self, index_of_func, arity = 2):
        self.function = self.functions[index_of_func]
        self.arity = arity

    def random_function():
        index = int(uniform(0, 3))
        return Function(index)

    def arity(self):
        return self.arity

    def __str__(self):
        return "Function: {0}, arity: {1}".format(self.function, str(self.arity))
