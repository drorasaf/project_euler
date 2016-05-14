import euler.euler50 as euler


def test_primes_sum():
    primes_sum = euler.generate_primes_sum([2, 3, 5, 7, 11, 13])
    assert primes_sum == [2, 5, 10, 17, 28, 41]


def test_binary_search():
    array = [1, 3, 5, 7, 10]
    assert euler.binary_search(array, 5)
    assert not euler.binary_search(array, 8)


def test_solution():
    assert euler.solution() == 997651
