"""
HigherMath
A simple mathematics library made from scratch using Python.

No external libraries are required.
"""

# ============================================================
# CONSTANTS
# ============================================================

pi = 3.141592653589793
tau = 2 * pi
e = 2.718281828459045

sets = {
    "N": "Natural Numbers",
    "W": "Whole Numbers",
    "Z": "Integers",
    "Q": "Rational Numbers",
    "I": "Irrational Numbers",
    "R": "Real Numbers"
}


# ============================================================
# BASIC OPERATIONS
# ============================================================

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return a minus b."""
    return a - b


def product(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(a, b):
    """Return a raised to the power b."""
    return a ** b


# ============================================================
# ROOTS
# ============================================================

def sqrt(a, tolerance=1e-12):
    """
    Calculate the square root using Newton's method.
    """
    if a < 0:
        raise ValueError("Square root of a negative number is not real.")

    if a == 0:
        return 0

    x = a if a >= 1 else 1

    while True:
        next_x = (x + a / x) / 2

        if abs(next_x - x) < tolerance:
            return next_x

        x = next_x


def cbrt(a, tolerance=1e-12):
    """
    Calculate the cube root using Newton's method.
    """
    if a == 0:
        return 0

    sign = 1

    if a < 0:
        sign = -1
        a = -a

    x = a if a >= 1 else 1
 
    while True:
        next_x = (2 * x + a / (x * x)) / 3

        if abs(next_x - x) < tolerance:
            return sign * next_x

        x = next_x


# ============================================================
# FACTORIAL / COMBINATORICS
# ============================================================

def factorial(n):
    """Return n!."""
    if not isinstance(n, int):
        raise TypeError("Factorial requires an integer.")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1

    for i in range(2, n + 1):
        result *= i

    return result


def combinations(n, r):
    """Return nCr."""
    if not isinstance(n, int) or not isinstance(r, int):
        raise TypeError("n and r must be integers.")

    if r < 0 or n < 0 or r > n:
        raise ValueError("Invalid values for combinations.")

    return factorial(n) // (factorial(r) * factorial(n - r))


def permutations(n, r):
    """Return nPr."""
    if not isinstance(n, int) or not isinstance(r, int):
        raise TypeError("n and r must be integers.")

    if r < 0 or n < 0 or r > n:
        raise ValueError("Invalid values for permutations.")

    return factorial(n) // factorial(n - r)


# ============================================================
# ABSOLUTE VALUE / DISTANCE
# ============================================================

def absolute(a):
    """Return the absolute value of a."""
    if a < 0:
        return -a
    return a


def hypot(a, b):
    """Return sqrt(a² + b²)."""
    return sqrt(a * a + b * b)


def distance(point1, point2):
    """
    Calculate distance between two points.

    Example:
        distance([0, 0], [3, 4]) -> 5
    """
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimensions.")

    total = 0

    for a, b in zip(point1, point2):
        total += (b - a) ** 2

    return sqrt(total)


# ============================================================
# FIBONACCI
# ============================================================

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n < 0:
        raise ValueError("n cannot be negative.")

    if n == 0:
        return 0

    if n == 1:
        return 1

    a = 0
    b = 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


# ============================================================
# SIGN / REMAINDER
# ============================================================

def copysign(a, b):
    """
    Return the magnitude of a with the sign of b.
    """
    if b < 0:
        return -absolute(a)

    return absolute(a)


def remainder(a, b):
    """Return the remainder after division."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a % b


def raisee(a, b):
    """Alias for power()."""
    return a ** b


def reciprocal(a):
    """Return 1/a."""
    if a == 0:
        raise ZeroDivisionError("Cannot take reciprocal of zero.")

    return 1 / a


# ============================================================
# ANGLE CONVERSION
# ============================================================

def degrees(radians):
    """Convert radians to degrees."""
    return radians * 180 / pi


def radians(degree):
    """Convert degrees to radians."""
    return degree * pi / 180


# ============================================================
# TRIGONOMETRY
# ============================================================

def _normalize_angle(x):
    """
    Keep an angle within approximately -pi to pi.
    """
    x = x % tau

    if x > pi:
        x -= tau

    return x


def sin(x, terms=15):
    """
    Calculate sine using the Taylor series.

    x must be in radians.
    """
    x = _normalize_angle(x)

    result = 0

    for n in range(terms):
        power_value = x ** (2 * n + 1)
        sign = (-1) ** n
        result += sign * power_value / factorial(2 * n + 1)

    return result


def cos(x, terms=15):
    """
    Calculate cosine using the Taylor series.

    x must be in radians.
    """
    x = _normalize_angle(x)

    result = 0

    for n in range(terms):
        power_value = x ** (2 * n)
        sign = (-1) ** n
        result += sign * power_value / factorial(2 * n)

    return result


def tan(x):
    """Calculate tangent. x must be in radians."""
    c = cos(x)

    if absolute(c) < 1e-12:
        raise ValueError("Tangent is undefined at this angle.")

    return sin(x) / c


def cosec(x):
    """Calculate cosecant. x must be in radians."""
    s = sin(x)

    if absolute(s) < 1e-12:
        raise ValueError("Cosecant is undefined at this angle.")

    return 1 / s


def sec(x):
    """Calculate secant. x must be in radians."""
    c = cos(x)

    if absolute(c) < 1e-12:
        raise ValueError("Secant is undefined at this angle.")

    return 1 / c


def cot(x):
    """Calculate cotangent. x must be in radians."""
    s = sin(x)

    if absolute(s) < 1e-12:
        raise ValueError("Cotangent is undefined at this angle.")

    return cos(x) / s


# ============================================================
# INVERSE TRIGONOMETRY
# ============================================================

def arctan(x, terms=50):
    """
    Calculate arctangent using a series.

    For values outside [-1, 1], identities are used
    to improve convergence.
    """

    if x > 1:
        return pi / 2 - arctan(1 / x)

    if x < -1:
        return -pi / 2 - arctan(1 / x)

    result = 0

    for n in range(terms):
        result += ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)

    return result


def arcsine(x):
    """
    Calculate arcsine using arctangent.
    """
    if x < -1 or x > 1:
        raise ValueError("arcsine requires -1 <= x <= 1.")

    if x == 1:
        return pi / 2

    if x == -1:
        return -pi / 2

    return arctan(x / sqrt(1 - x * x))


def arccos(x):
    """
    Calculate arccosine using arcsine.
    """
    if x < -1 or x > 1:
        raise ValueError("arccos requires -1 <= x <= 1.")

    return pi / 2 - arcsine(x)


# ============================================================
# EXPONENTIAL / LOGARITHMS
# ============================================================

def exp(x, terms=50):
    """
    Calculate e^x using the Taylor series.
    """
    result = 1
    term = 1

    for n in range(1, terms):
        term *= x / n
        result += term

    return result


def log(x, base=e, tolerance=1e-12):
    """
    Calculate logarithm using Newton's method.

    Default base is e.
    """
    if x <= 0:
        raise ValueError("Logarithm requires x > 0.")

    if base <= 0 or base == 1:
        raise ValueError("Invalid logarithm base.")

    # Find ln(x)
    # Solve e^y = x
    if x == 1:
        natural_log = 0
    else:
        y = x - 1 if x < 2 else 1

        for _ in range(100):
            ey = exp(y)
            next_y = y - (ey - x) / ey

            if absolute(next_y - y) < tolerance:
                break

            y = next_y

        natural_log = next_y

    if base == e:
        return natural_log

    # Calculate ln(base)
    y = base - 1 if base < 2 else 1

    for _ in range(100):
        ey = exp(y)
        next_y = y - (ey - base) / ey

        if absolute(next_y - y) < tolerance:
            break

        y = next_y

    return natural_log / next_y


# ============================================================
# PRIME NUMBERS
# ============================================================

def is_prime(n):
    """Return True if n is prime."""
    if not isinstance(n, int):
        return False

    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    i = 3

    while i * i <= n:
        if n % i == 0:
            return False

        i += 2

    return True


def primeNumbers(limit):
    """
    Return all prime numbers from 2 to limit.
    """
    if limit < 2:
        return []

    primes = []

    for n in range(2, limit + 1):
        if is_prime(n):
            primes.append(n)

    return primes


# ============================================================
# NUMBER LISTS
# ============================================================

def multiplicationTable(n, upto=10):
    """Return the multiplication table of n."""
    return [n * i for i in range(1, upto + 1)]


def squares(n):
    """Return squares from 1 to n."""
    if n < 1:
        return []

    return [i ** 2 for i in range(1, n + 1)]


def cubes(n):
    """Return cubes from 1 to n."""
    if n < 1:
        return []

    return [i ** 3 for i in range(1, n + 1)]


def powerTillX(a, x):
    """
    Return powers of a from a^1 to a^x.
    """
    if x < 1:
        return []

    return [a ** i for i in range(1, x + 1)]


# ============================================================
# STATISTICS
# ============================================================

def maximum(values):
    """Return the largest value."""
    if len(values) == 0:
        raise ValueError("Cannot find maximum of an empty list.")

    largest = values[0]

    for value in values[1:]:
        if value > largest:
            largest = value

    return largest


def minimum(values):
    """Return the smallest value."""
    if len(values) == 0:
        raise ValueError("Cannot find minimum of an empty list.")

    smallest = values[0]

    for value in values[1:]:
        if value < smallest:
            smallest = value

    return smallest


def mean(values):
    """Return the arithmetic mean."""
    if len(values) == 0:
        raise ValueError("Cannot calculate mean of an empty list.")

    total = 0

    for value in values:
        total += value

    return total / len(values)


def median(values):
    """Return the median."""
    if len(values) == 0:
        raise ValueError("Cannot calculate median of an empty list.")

    data = sorted(values)
    n = len(data)

    middle = n // 2

    if n % 2 == 1:
        return data[middle]

    return (data[middle - 1] + data[middle]) / 2


def mode(values):
    """Return the most frequent value."""
    if len(values) == 0:
        raise ValueError("Cannot calculate mode of an empty list.")

    counts = {}

    for value in values:
        if value not in counts:
            counts[value] = 1
        else:
            counts[value] += 1

    highest_count = 0
    most_common = values[0]

    for value in counts:
        if counts[value] > highest_count:
            highest_count = counts[value]
            most_common = value

    return most_common


# ============================================================
# ARITHMETIC PROGRESSIONS
# ============================================================

def AP(first, difference, n):
    """
    Return the nth term of an arithmetic progression.
    """
    if n < 1:
        raise ValueError("n must be at least 1.")

    return first + (n - 1) * difference


def AP_sum(first, difference, n):
    """
    Return the sum of the first n terms of an AP.
    """
    if n < 1:
        raise ValueError("n must be at least 1.")

    return n * (2 * first + (n - 1) * difference) / 2


# ============================================================
# GEOMETRIC PROGRESSIONS
# ============================================================

def GP(first, ratio, n):
    """
    Return the nth term of a geometric progression.
    """
    if n < 1:
        raise ValueError("n must be at least 1.")

    return first * ratio ** (n - 1)


def GP_sum(first, ratio, n):
    """
    Return the sum of the first n terms of a GP.
    """
    if n < 1:
        raise ValueError("n must be at least 1.")

    if ratio == 1:
        return first * n

    return first * (ratio ** n - 1) / (ratio - 1)


# ============================================================
# MAIN TESTS
# ============================================================

if __name__ == "__main__":

    print("===== HigherMath =====")

    print("pi =", pi)
    print("e =", e)
    print("tau =", tau)

    print("\nBasic Operations")
    print("add(5, 3) =", add(5, 3))
    print("subtract(5, 3) =", subtract(5, 3))
    print("product(5, 3) =", product(5, 3))
    print("divide(5, 3) =", divide(5, 3))
    print("power(5, 3) =", power(5, 3))

    print("\nRoots")
    print("sqrt(25) =", sqrt(25))
    print("cbrt(27) =", cbrt(27))

    print("\nFactorial")
    print("factorial(5) =", factorial(5))

    print("\nCombinations")
    print("10C3 =", combinations(10, 3))
    print("10P3 =", permutations(10, 3))

    print("\nFibonacci")
    print("Fibonacci(10) =", fibonacci(10))

    print("\nTrigonometry")
    print("sin(90°) =", sin(radians(90)))
    print("cos(0°) =", cos(radians(0)))
    print("tan(45°) =", tan(radians(45)))

    print("\nPrime Numbers")
    print(primeNumbers(50))

    print("\nStatistics")

    numbers = [2, 4, 4, 6, 8]

    print("Numbers:", numbers)
    print("Maximum:", maximum(numbers))
    print("Minimum:", minimum(numbers))
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))

    print("\nLogarithm")
    print("log(e) =", log(e))
    print("log(100, 10) =", log(100, 10))

    print("\nAP")
    print("10th term:", AP(2, 3, 10))
    print("Sum:", AP_sum(2, 3, 10))

    print("\nGP")
    print("10th term:", GP(2, 2, 10))
    print("Sum:", GP_sum(2, 2, 10))

    print("\nHigherMath loaded successfully!")
