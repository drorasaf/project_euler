import euler.euler46 as euler


def test_is_int_twice_squared():
    assert euler.is_int_twice_squared(2)
    assert euler.is_int_twice_squared(8)


def test_smallest_non_gb_odd_composite():
    assert euler.smallest_non_gb_odd_composite(100, 2) is None
    assert euler.smallest_non_gb_odd_composite(100, 3) is None


def test_solution():
    assert euler.solution() == 5777
