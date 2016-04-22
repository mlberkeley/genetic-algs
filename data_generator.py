
import numpy as np
import pickle

""" Module to generate fake data to test the program. """

def make_pendulum(m, l, angle_0, t=10, sample_period=1e-2, fname="pendulum.pkl"):
    """ Simulate a pendulum with mass `m` and length `l` starting at
        angle `angle_0` relative to the vertical.

        Args:
            m: mass (in kg)
            l: length (in m)
            angle_0: initial angle (in radians)
            t: time to run the simulation (in seconds) (default=10)
            sample_period: time period of each sample (in seconds) (default=1e-2)
            fname: filename to save .pkl file to (default="pendulum.pkl")

        Outputs:
            pickled dictionary file with the following mappings:
            "x": x position of the pendulum (right is positive)
            "y": y position of the pendulum (up is positive)
            "sample_period": time per sample (in seconds)
    """
    # Solution to the system is theta = Acos(wt)
    g = 9.81

    times = np.arange(0, t, sample_period)

    angular_freq = np.sqrt(g / l)
    xs = []
    ys = []
    for time in times:
        angle = angle_0 * np.cos(angular_freq * time)

        x = l * np.sin(angle)
        y = l * np.cos(angle)

        xs.append(x)
        ys.append(y)

    xs = np.array(xs)
    ys = np.array(ys)

    # Save data
    data = {}
    data["arrays"] = {}
    data["arrays"]["t"] = times
    data["arrays"]["x"] = xs
    data["arrays"]["y"] = ys

    # Save sample period
    data["sample_period"] = sample_period

    pickle.dump(data, open(fname, "wb"))

if __name__ == "__main__":
    make_pendulum(1, 10, 1, t=0.1)
