
""" Module to plot files generated from data_generator.py. """

import numpy as np
import matplotlib.pyplot as plt
import pickle

def plot(fname):
    m = pickle.load(open(fname, "rb"))

    # Load sample period
    sample_period = m["sample_period"]
    arrays = m["arrays"]

    for k, v in arrays.items():
        times = np.linspace(0, len(v) * sample_period, len(v))

        plt.figure()
        plt.title(fname)
        plt.xlabel("Time (s)")
        plt.ylabel(k)
        plt.plot(times, v)

        plt.savefig("images/{0}_{1}.png".format(fname[:-4], k))

    plt.show()

if __name__ == "__main__":
    #plot("pendulum.pkl")
    #plot("linear.pkl")
    plot("quadratic.pkl")
