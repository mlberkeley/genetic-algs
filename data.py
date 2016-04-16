
class Data(object):
    """ Data object holds arrays of variables over time. """
    def __init__(fname, sample_freq=44100):
        # TODO
        # Load all variables and computes derivatives
        # Stores it in dictionary
        self._data = {}
        self._sample_freq = sample_freq

    def times(self):
        """ Returns a linspace of times to be evaluated.

            Returns:
                numpy array of floats
        """
        samples = len(self._data["t"])  # TODO clean this up
        period = 1 / self.sample_freq
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
    # TODO test
    pass
