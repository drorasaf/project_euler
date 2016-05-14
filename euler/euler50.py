import primesieve
import bisect
import logging

log = logging.getLogger()


def generate_primes_sum(primes_array):
    """ Returns a list of the cumulative sum of all primes """
    primes_sum = [primes_array[0]]
    for i in range(1, len(primes_array)):
        primes_sum.append(primes_array[i] + primes_sum[i-1])

    return primes_sum


def binary_search(sorted_array, x):
    """ Returns True if the value x is inside the specified sorted_array """
    index = bisect.bisect_left(sorted_array, x)
    if index != len(sorted_array) and sorted_array[index] == x:
        return True
    return False


def search_cumulative_primes(max_range):
    """ Search for the first cumulative """
    log.info("Start looking for cumulative primes: %d" % max_range)
    res = None
    num_of_primes = 0

    primes = primesieve.generate_primes(max_range)
    primesum = generate_primes_sum(primes)

    # check for every cumulative sum, every possible sum of primes
    for i in range(len(primesum)):
        j = i - (num_of_primes + 1)

        while j > 0:
            prime_candidate = primesum[i] - primesum[j]
            if prime_candidate > max_range:
                break
            if binary_search(primes, prime_candidate):
                num_of_primes = i - j
                res = prime_candidate
            j = j - 1

    return res


def solution():
    """ Returns the answer as requested by the euler project problem """
    max_range = 10 ** 6
    return search_cumulative_primes(max_range)
