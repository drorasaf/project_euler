import primesieve


def primesum

def cumulative_primes(max_range):
    primesum = primesieve.primesum(max_range)


def solution():
    """ Returns the answer as requested by the euler project problem """
    max_range = 10 ** 6
    return cumulative_primes(max_range)
