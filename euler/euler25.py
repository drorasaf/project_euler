import os
import scipy.constants
import numpy as np


def fibonacci_digits(digits):
    """ Returns the amount of iterations required to get to
        the number of digits

        Input: Number of digits the fibonacci number should have
    """
    phi = scipy.constants.golden
    n = np.ceil((np.log(10) * (digits - 1) + np.log(5) / 2) / np.log(phi))

    return int(n)


def solution():
    """ Returns the answer as requested by the euler project problem """
    required_digits = 1000
    return fibonacci_digits(required_digits)
