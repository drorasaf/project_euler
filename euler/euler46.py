import math
import primesieve
import logging

log = logging.getLogger()


def generate_primes(max_range, min_range=2):
    return primesieve.generate_primes(min_range, max_range)


def is_int_twice_squared(squared):
    """ Returns True if number is a perfect square, otherwise False
        Input: Integer
    """
    x = math.sqrt(squared/2)
    return x == int(x)


def smallest_non_gb_odd_composite(max_range, min_range):
    """ Goldbach's theorem conjucts that odd composite numbers are the sum of
        a prime number and twice the square of a prime.
        This fuction gets a max_range which is the upper bound for the
        exhausive search.
    """
    log.info("Start exhausive search from %d to %d" % (min_range, max_range))
    if min_range % 2 == 0:
        odd_num = min_range + 1
    else:
        odd_num = min_range
    found = False

    prime_list = generate_primes(max_range, min_range)

    while (odd_num < max_range) and not found:
        odd_num += 2
        j = 0

        found = True
        while (odd_num >= prime_list[j]):
            if is_int_twice_squared(odd_num - prime_list[j]):
                found = False
                break
            j += 1

    log.info("found %d odd_num %d" % (found, odd_num))
    return odd_num if found else None


def solution():
    """ Returns the answer as requested by the euler project problem """
    max_range = 10 ** 5
    return smallest_non_gb_odd_composite(max_range, 0)
