
import sympy as sy
import numpy as np

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

    @staticmethod
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

        # Add 0-ary functions
        function_set[0] = [t]

        # Add 2-ary functions
        function_set[2] = [add, mul]

        all_functions = function_set[0] + function_set[2]

        PROB_FLOAT = 0.1

        if arity is not None:
            if arity == 0:
                if np.random.random() < PROB_FLOAT:
                    return Function.random_float()
                else:
                    return choice(function_set[arity])
            else:
                return choice(function_set[arity])
        else:
            if np.random.random() < PROB_FLOAT:
                return Function.random_float()
            else:
                return choice(all_functions)

    @staticmethod
    def random_terminal():
        """ Return a random terminal (can be either a terminal or
            intermediate node.

            Returns:
                0-ary Function
        """
        return Function.random_function(arity=0)

    @staticmethod
    def random_float(interval=(0, 10)):
        """ Return a random float function within the interval.
            
            Args:
                interval: 2-tuple in the format (min, max)

            Returns:
                0-ary Function
        """
        min_, max_ = interval
        x = np.random.uniform(min_, max_)

        func = Function.make_float_function(x)
        return Function(func, 0, str(x))

    @staticmethod
    def make_float_function(x):
        """ Returns a sympy Function that constructs a Float.

            Args:
                x: Float

            Returns:
                sympy Function
        """
        return sy.Lambda((), x)

    def __str__(self):
        return self.label

class Time(sy.Function):
    @classmethod
    def eval(cls):
        return sy.Symbol("t")

t = Function(Time, 0, "t")
add = Function(sy.add.Add, 2, "+")
mul = Function(sy.add.Mul, 2, "*")

if __name__ == "__main__":
    test(0, Function.make_float_function(0)(), "0")
    test(7, add.evaluate(3, 4), "3 + 4")
