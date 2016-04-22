
import sympy as sy

from random import choice

from test import test

class Function(object):
    """ A Function is an object that acts as a wrapper over lambda
        functions, that contains information such as arity.

        Constants are Functions with 0-arity.
    """
    def __init__(self, func, arity=None, label="f"):
        """ Function constructor.

            Args:
                func: sympy Function or Symbol
                arity: int (constraint on arguments) (default=None)
                label: name for function (default="f")

            Returns:
                Function object
        """
        self.func = func
        self.arity = arity
        self.label = label

    def evaluate(self, *args):
        if self.arity == 0:
            return self.func()
        else:
            return self.func(*args)

    def random_function(arity=None):
        """ Return a random function (can be either a terminal or
            intermediate node) with the specified arity (None means
            no arity constraint).

            Args:
                arity: integer representing arity (default=None)

            Returns:
                Function
        """
        # TODO clean
        function_set = {}
        function_set[0] = [zero, one, t]
        function_set[2] = [add, mul]

        all_functions = [zero, one, t, add, mul]

        if arity:
            return choice(function_set[arity])
        else:
            return choice(all_functions)

    def random_terminal():
        """ Return a random terminal (can be either a terminal or
            intermediate node.

            Returns:
                0-ary Function
        """
        return Function.random_function(arity=0)

    def __str__(self):
        return self.label

class Zero(sy.Function):
    @classmethod
    def eval(cls):
        return sy.Float(0)

class One(sy.Function):
    @classmethod
    def eval(cls):
        return sy.Float(1)

class Mul(sy.Function):
    @classmethod
    def eval(cls, x, y):
        return x * y

class Time(sy.Function):
    @classmethod
    def eval(cls):
        return sy.Symbol("t")

zero = Function(Zero, 0, "0")
one = Function(One, 0, "1")
t = Function(Time, 0, "t")
add = Function(sy.add.Add, 2, "+")
mul = Function(sy.add.Mul, 2, "*")

if __name__ == "__main__":
    test(0, zero.evaluate(), "0")
    test(1, one.evaluate(), "1")
    test(7, add.evaluate(3, 4), "3 + 4")
