import math
try:
    import numpy as np
except ImportError:
    pass
sets = {
    "A" : "The Primary Letter Used For Any Set",
    "N" : "Natural Numbers",
    "Z" : "Integers",
    "Z+" : "Positive Integers" ,
    "Q" : "Rational Numbers",
    "Q+" : "Positive Rational Numbers",
    "T" : "Irratioal Numbers",
    "R" : "Real Numbers",
    "R+" : "Positive Real Numbers",
    "C" : "Complex Numbers",
    }
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def product(a,b):
    return a*b
def divide(a,b):
    return a/b
def power(a,b):
    return a**b
def sqrt(a):
    return round(a**0.5,0)
def cbrt(a):
    return round(a**0.333,0)
def pi():
    return 3.141592653589793
def tau():
    return 3.141592653589793*2
def factorial(a):
    if a<0:
        print("Can't find factorial of negative numbers")
        return
    if a ==0:
        a = 1
    else:
        a *= factorial(a-1)
    return a
def hypot(a,b):
    c = (a**2+b**2)**0.5
    return int(c)
def e():
    return 2.718281828459045
def absolute(a):
    if a < 0:
        b = str(float(a))
        c = b.lstrip("-")
        d = float(c)
    else:
        d = float(a)
    return d
def combinations(n,r):
    return int(factorial(n)/(factorial(r)*factorial((n-r))))
def permutations(n,r):
    return int(factorial(n)/factorial((n-r)))
def fibbion(term):
    a = 1
    b = 0
    c = []
    for _ in range(term):
        a,b = b,a+b
        c.append(a)
    return c[-1]
def truncate(a):
    return int(a)
def distance(p,q):
    return sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
def copysign(a,b):
    if b < 0:
        return -abs(a)
    else:
        return abs(a)
def raisee(a):
    return round(e()**a,12)
def remainder(a,b):
    return float(a%b)
def to_radian(degrees):
    return degrees * (pi()/180)
def to_degrees(radian):
    return radian * (180/pi())
def maxValue(array):
    return max(array)
def minValue(array):
    return min(array)
def mean(array):
    return sum(array)/len(array)
def median(array):
    sorted_data = sorted(array)
    n = len(sorted_data)
    mid = n//2
    if n%2 == 0:
        median_val = (sorted_data[mid-1]+sorted_data[mid])/2.0
    else:
        median_val = sorted_data[mid]
    return median_val
def mode(array):
    counts = {}
    for val in array:
        rounded_val = round(val,6)
        counts[rounded_val] = counts.get(rounded_val,0)+1
    max_count = max(counts.values())
    mode_val = [val for val,count in counts.items() if count == max_count]
    return mode_val[0]
def sin(x):
    if x == 0:
        return 0
    elif x == 30:
        return 1/2
    elif x == 45:
        return math.sqrt(2)/2
    elif x == 60:
        return math.sqrt(3)/2
    elif x == 90:
        return 1
    else:
        x = x%(2 * pi())
        if x > pi():
            x -= 2 * pi()
        term = x
        sin_x = x
        for n in range(1,10):
            term *= -x*x / ((2*n)*(2*n+1))
            sin_x += term
        return sin_x
def cos(x):
    if x == 0:
        return 1
    elif x == 30:
        return eval("3**0.5/2")
    elif x == 45:
        return sqrt(2)/2
    elif x == 60:
        return 1/2
    elif x == 90:
        return 0
    else:
        x = x%(2* pi())
        if x > pi():
            x -= 2 * pi()
        term = 1
        cos_x = 1
        for n in range(1,10):
            term *= -x * x / ((2*n-1)*(2*n))
            cos_x += term
        return cos_x
def tan(x):
    c = (x)
    s = sin(x)
    if c == 0:
        return
    return s/c
def cosec(x):
    return 1/sin(x)
def sec(x):
    return 1/cos(x)
def cot(x):
    c = cos(x)
    s = sin(x)
    if s == 0:
        return
    return s/c
def arcsine(x):
    return math.asin(x)
def arccos(x):
    asin_val = arcsine(x)
    if asin_val is None:
        return None
    return (pi()/2.0) - asin_val
def arctan(x):
    return math.atan(x)
def AP(seq,term):
    ft = seq[0]
    st = seq[1]
    cd = st-ft
    reqTerm = ft+(term-1)*cd
    return reqTerm
def GP(seq,term):
    cr = seq[1]/seq[0]
    a = seq[0]
    reqTerm = a*(cr ** (term-1))
    return reqTerm
def primeNumbers(term):
    primeNumbers = set()
    for i in range(term):
        primeNumbers.add(2)
        primeNumbers.add(3)
        primeNumbers.add(5)
        primeNumbers.add(7)
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            primeNumbers.add(i)
    return primeNumbers
def multiplicationTable(num):
    i = []
    for x in range(1,11):
        i.append(num*x)
    return i
def squares():
    squares = [x**2 for x in range(101)]
    return squares
def cubes():
    cubes = [x**3 for x in range(101)]
    return cubes
def powerTillX(x):
    power = [y**x for y in range(101)]
    return power
def reciprocal(x):
    reciprocal = x**-1
    return reciprocal
def log(x,base = None):
    if base is None:
        base = e()
    return math.log(x,base)
if __name__ == "__main__":
    a = e()
    print(a)