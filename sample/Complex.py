factorial = (lambda f: f(f))(
    lambda m: (lambda n:
        1 if n == 0 else n * m(m)(n - 1)))

print(factorial(5))