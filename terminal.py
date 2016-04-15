
from random import uniform

class Terminal(object):
    def __init__(self, num=None):
        self.num = num

    @staticmethod
    def random_terminal():
        # Right now only random numbers from 0 to 100
        num = uniform(0, 100)
        return Terminal(num)

    def __str__(self):
        return "Terminal: {0}".format(self.num)
