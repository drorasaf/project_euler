from euler import euler25 as fib_digits


def test_fibonnnaci_digits_math_correct():
    num_2digit = fib_digits.fibonacci_digits(2)
    assert num_2digit == 7

    num_3digit = fib_digits.fibonacci_digits(3)
    assert num_3digit == 12


def test_solution():
    num1000digit = fib_digits.solution()
    assert num1000digit == 4782
