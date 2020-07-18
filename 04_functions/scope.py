import sys


def wrapper(outer):
    """
    Define and return functions
    Inner function has access to outer function params
    """
    def identity(x):
        print("outer = {}".format(outer))
        return x
    return identity


def first_class():
    """
    :return: Other function
    """
    identifier = wrapper("boo")
    print("identifier(42) = {}".format(identifier(42)))


def scopes():
    """
    Show scopes
    Global variables shadow builtin functions
    'min = 42' hides min()
    """
    print("Builtin scope: min(42, 0)")
    x = min(42, 0)
    print(min, "=", x)
    print("Global scope: MIN_GLOBAL = {}".format(MIN_GLOBAL))

    def inner():
        print("Enclosing scope: inner()")
        # noinspection PyShadowingNames
        x = 42
        print("x=", x)
        print("Local scope: x = 42")

    inner()
    print("Dynamic search performed: global variable MIN_GLOBAL declared after scopes(), but found as inner->global")


MIN_GLOBAL = 42


def explicit():
    """
    Explicit access to global, enclosing and local scope
    """
    x = 42
    print("globals():", globals())
    print("locals():", locals())

    # if local variable use '=' operator, if shadow global
    # noinspection PyPep8Naming
    # noinspection PyShadowingNames
    MIN_GLOBAL = 1
    print("Shadow MIN_GLOBAL = {}".format(MIN_GLOBAL))


def show_global():
    """
    Always access
    """
    print("global MIN_GLOBAL = {}".format(MIN_GLOBAL))


def use_global():
    global MIN_GLOBAL
    MIN_GLOBAL = 24
    print("Explicit access:")
    show_global()


def cell(value):
    """
    Example of usage nonlocal
    This keyword allows changing value from enclosing function scope
    Like with 'global', simple access possible without keyword
    """
    def getter():
        return value

    def setter(new_value):
        nonlocal value
        value = new_value

    return getter, setter


def use_nonlocal():
    getter, setter = cell(42)
    print("getter(): {}".format(getter()))
    setter(24)
    print("setter(24)")
    print("Again getter(): {}".format(getter()))


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
