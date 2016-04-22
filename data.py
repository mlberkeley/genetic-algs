
""" Module to hold the Data class, which holds information that can be looked
    up using the `get` method.
"""

import pickle
import numpy as np

class Data(object):
    """ Data object holds arrays of variables over time. """
    def __init__(self, fname):
        # TODO
        # Load all variables and computes derivatives
        # Stores it in dictionary

        pkl_obj = pickle.load(open(fname, "rb"))

        self._data = pkl_obj["arrays"]
        self._sample_period = pkl_obj["sample_period"]

    def times(self):
        """ Returns a linspace of times to be evaluated.

            Returns:
                numpy array of floats
        """
        samples = len(self._data["t"])  # TODO clean this up
        period = self._sample_period
        return np.linspace(0, period * samples, samples)

    def variables(self):
        """ Return all variables in data.

            Returns:
                list of variable names
        """
        return self._data.keys()

    def get(self, var):
        """ Takes in a variable name and returns the data
            array associated with it.
        """
        return self._data[var]

if __name__ == "__main__":
    data = Data("pendulum.pkl")
