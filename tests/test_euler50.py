import euler.euler50 as euler


def test_primes_sum():
    primes_sum = euler.generate_primes_sum([2, 3, 5, 7, 11, 13])
    assert primes_sum == [2, 5, 10, 17, 28, 41]


def test_solution():
    assert euler.solution() == 997651
