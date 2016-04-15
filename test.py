
""" Test suite. """

def test(expected, actual, name=None, pred=lambda exp, act: exp == act):
    """ Runs a test and prints result.

        Args:
            expected: expected value from test
            actual: actual value from test
            name: name for test (default=None)
            pred: function that takes two values and returns True if they
                  are close enough to pass the test, or False otherwise

        Returns:
            None

        Outputs:
            String determining whether test passes or fails
    """
    if expected == actual:
        print("PASSED test '{0}': expected {1}, got {2}".format(name, expected,
                                                                actual))
    else:
        print("FAILED test '{0}': expected {1}, got {2}".format(name, expected,
                                                                actual))
