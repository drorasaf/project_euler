import math
import primesieve


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
    import datetime
    if min_range % 2 == 0:
        odd_num = min_range + 1
    else:
        odd_num = min_range
    not_found = True

    a = datetime.datetime.now()
    prime_list = generate_primes(max_range, min_range)
    b = datetime.datetime.now()
    print ("generate prime list: " + str(b-a))

    while (odd_num < max_range) and not_found:
        odd_num += 2
        j = 0

        not_found = False
        while (odd_num >= prime_list[j]):
            if is_int_twice_squared(odd_num - prime_list[j]):
                not_found = True
                break
            j += 1

    c = datetime.datetime.now()
    print ("search for smallest number took " + str(c-b))
    return odd_num if not_found else None


def solution():
    """ Returns the answer as requested by the euler project problem """
    max_range = 10 ** 5
    smallest_non_gb_odd_composite(max_range, 0)

print(solution())
