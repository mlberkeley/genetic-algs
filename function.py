
from test import test

class Function(object):
    """ A Function is an object that acts as a wrapper over lambda
        functions, that contains information such as arity.

        Constants are Functions with 0-arity.
    """
    def __init__(self, func, arity=None, label="f"):
        self.func = func
        self.arity = arity
        self.label = label

    def evaluate(self, *args):
        return self.func(*args)

    def random_function():
        """ Return a random function (can be either a terminal or
            intermediate node.

            Returns:
                Function
        """
        # TODO
        pass

    def __str__(self):
        return self.label

zero = Function(lambda: 0, 0, "0")
one = Function(lambda: 1, 0, "1")
add = Function(lambda a, b: a + b, 2, "+")
sub = Function(lambda a, b: a - b, 2, "-")

if __name__ == "__main__":
    test(0, zero.evaluate(), "0")
    test(1, one.evaluate(), "1")
    test(7, add.evaluate(3, 4), "3 + 4")
