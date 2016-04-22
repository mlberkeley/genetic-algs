
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
        if arity is None:
            functions = [add]
            return choice(functions)
        elif arity == 0:
            return choice([zero, one])
        elif arity == 2:
            return choice([add])
        else:
            print("ERROR")

    def random_terminal():
        """ Return a random terminal (can be either a terminal or
            intermediate node.

            Returns:
                0-ary Function
        """
        functions = [zero, one]
        return choice(functions)

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

zero = Function(Zero,  0, "0")
one =  Function(One,   0, "1")
add =  Function(sy.add.Add, 2, "+")

if __name__ == "__main__":
    test(0, zero.evaluate(), "0")
    test(1, one.evaluate(), "1")
    test(7, add.evaluate(3, 4), "3 + 4")
