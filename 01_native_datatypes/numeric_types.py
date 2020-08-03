import fractions
import math
import sys
import cmath


def boolean():
    """
    Evaluate boolean
    """
    print('Evaluate boolean')
    size = 0
    # The result of the expression size < 0 is always a boolean
    print("size > 0 is", size > 0)
    print("size == 0 is", size == 0)
    print('Boolean implicitly converted to int, 42 + True =', 42 + True)
    # Falsy args, or args converted to False: None, 0, [], (), {}, set()


def walrus():
    """
    The purpose of the walrus operator is to consolidate an assignment statement
    and a boolean expression, assigning value to variable within the expression
    Operator has analog in C
    if (int i = length())
    Parenthesis are critical for to evaluate properly!
    """
    # before
    my_list = [1, 2, 3, 4, 5]
    print("BEFORE: if len(my_list) > 3:")
    if len(my_list) > 3:
        n = len(my_list)
        print(f"The list is too long with {n} elements")

    # after
    print("AFTER: if (n := len(my_list)) > 3:")
    if (n := len(my_list)) > 3:
        print(f"The list is too long with {n} elements")


def numbers():
    """
    Evaluate numbers

    Python is dynamically typed. Using return or declaration types is just a hint
    Hints are not:
    - Not static types. The language is not enforcing anything
    - Not Performance boosting
    """
    print('Evaluate numbers')

    # You can use the type() function to check the type of any value or variable
    # Similarly, you can use the isinstance() function
    # to check whether a value or variable is of a given type
    print("type(1) is", type(1))
    print("isinstance(1, int) is", isinstance(1, int))
    print("isinstance(1.0, float) is", isinstance(1.0, float))

    # Adding an int to a float yields a float
    print("type(1+1) is", type(1+1))
    print("type(1+1.0) is", type(1+1.0))

    # interesting twist - 'type' itself is object
    print("type(type(1)) is ", type(type(1)))

    # The value sys.maxsize reports the platform pointer size
    # Any integer too big to fit in 64 bits is handled in software
    print("sys.maxsize=", sys.maxsize)

    # infinity
    print('float("inf") = {}'.format(float("inf")))

    # combined compare
    x = math.pi
    if 0 < x < 10:
        print("x between 0 and 10")


def complex_num():
    c1 = 2 + 7j
    c2 = complex(3, 6)
    print("2 + 7j = {}; type = {}".format(c1, type(c1)))
    print("complex(3, 6) = {}; type = {}".format(c2, type(c2)))

    print("Addition of two complex number =", c1 + c2)
    print("Subtraction of two complex number =", c1 - c2)

    # complex numbers don’t support comparison operators like <, >, <=, =>
    # and it will through TypeError message

    # Phase is angle between the real axis and the vector representing the imaginary part
    print('Phase = {} radians'.format(cmath.phase(c1)))


def conversions():
    """
    Converts int<->float
    """
    print('Convert numbers')
    # The int() function will truncate, not round
    # The int() function truncates negative numbers towards 0.
    # I.e. it’s a true truncate function, not a floor function
    # Floating point numbers are accurate to 15 decimal places
    # Integers can be arbitrarily large

    # See strong typing
    a: float = 2.9
    print("int(2.9) =", int(a))
    print("int(-2.9) =", int(-a))
    very_long_int = 9999999999999999999
    print("type(9999999999999999999) is", type(very_long_int))


def operations():
    """
    Simple math operations
    """
    print('Simple operations')
    # The / operator performs floating point division
    # The // operator performs a quirky kind of integer division
    # When the result is positive, you can think of it as truncating (not rounding)
    print("11/2 =", 11/2)
    print("11//2 =", 11//2)

    # When integer-dividing negative numbers, the // operator rounds up to the nearest integer
    print("-11//2 =", -11//2)

    # The ** operator means raised to the power of
    print("4**2 =", 4**2)

    # The % operator gives the remainder after performing integer division
    print("11 % 2 =", 11 % 2)


def fraction():
    """
    Simple fraction
    """
    print('Simple fraction')

    # To start using fraction, import the fraction module
    x = fractions.Fraction(1, 3)
    print("Fraction(1, 3) =", x)

    # You can perform all the usual mathematical operations with fraction
    print("Fraction(1, 3)**2 =", x**2)

    # The Fraction object will automatically reduce fraction (6/4) = (3/2)
    # Python has the good sense not to create a fraction with a zero denominator
    y = fractions.Fraction(6, 4)
    print("Fraction(6, 4) =", y)


def constants():
    """
    Simple math constants
    """
    print('Simple math constants')
    print("pi =", math.pi)
    print("e =", math.e)
    print("tan(pi/4)=", math.tan(math.pi/4))


def else_forms():
    """
    'else' in the end if 'for', 'while', 'try' means fallback branch,
    which works if none of iterations were performed
    """
    items = []
    for item in items:
        print("Item = {}".format(item))
    else:
        print("Fallback branch")


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of module functions to call, e.g. operations")
