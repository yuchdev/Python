import fractions
import math
import sys


def boolean():
    """
    Evaluate boolean
    """
    print('####################################')
    print('Evaluate boolean')
    size = 0
    # The result of the expression size < 0 is always a boolean
    print("size > 0 is", size > 0)
    print("size == 0 is", size == 0)
    print('Boolean implicitly converted to int, 42 + True =', 42 + True)


def numbers():
    """
    Evaluate numbers
    """
    print('####################################')
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

    # interesting twist type itself is object
    print("type(type(1)) is ", type(type(1)))

    # The value sys.maxsize reports the platform pointer size
    # Any integer too big to fit in 64 bits is handled in software
    print("sys.maxsize=", sys.maxsize)


def conversions():
    """
    Converts int<->float
    """
    print('####################################')
    print('Convert numbers')
    # The int() function will truncate, not round
    # The int() function truncates negative numbers towards 0.
    # It’s a true truncate function, not a floor function
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
    print('####################################')
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


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call: boolean, number, conversions, operations, fraction, constant")
