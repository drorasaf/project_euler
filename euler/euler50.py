import primesieve
import logging

log = logging.getLogger()


def generate_primes_sum(primes_array):
    """ Returns a list of the cumulative sum of all primes """
    primes_sum = [primes_array[0]]
    for i in range(1, len(primes_array)):
        primes_sum.append(primes_array[i] + primes_sum[i-1])

    return primes_sum


def search_cumulative_primes(max_range):
    """ Search for the first cumulative """ 
    log.info("Start looking for cumulative primes: %d" % max_range)
    primes = primesieve.generate_primes(max_range)
    primesum = generate_primes_sum(primes)
    

def solution():
    """ Returns the answer as requested by the euler project problem """
    max_range = 10 ** 6
    return cumulative_primes(max_range)
