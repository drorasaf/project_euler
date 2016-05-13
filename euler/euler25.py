import os
import scipy.constants
import numpy as np


def fibonacci_digits_brute(digits):
    pass


def fibonacci_digits_math(digits):
    """ Returns the amount of iterations required to get to t
        he number of digits
    """
    phi = scipy.constants.golden
    n = np.ceil((np.log(10) * (digits - 1) + np.log(5) / 2) / np.log(phi))

    return int(n)
