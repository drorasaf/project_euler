import euler.fibonacci_digits as fib_digits

def test_fibonnnaci_digits_math_correct():
    num_2digit = fib_digits.fibonacci_digits_math(2)
    assert num_2digit == 7

    num_3digit = fib_digits.fibonacci_digits_math(2)
    assert num_3digit == 12
