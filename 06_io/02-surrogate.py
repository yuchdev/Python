import sys

__doc__ = """Show examples of debug print decorators.
From naive to production implementation.
"""


def surrogate_pair(symbol):
    """
    Convert a symbol to a surrogate pair
    Surrogate pairs are specific to UTF-16 encoding to handle characters
    beyond the Basic Multilingual Plane (BMP)
    """
    # Check if the symbol is within the BMP range (U+0000 to U+FFFF)
    if 0x0000 <= symbol <= 0xFFFF:
        return [symbol]  # This symbol doesn't require a surrogate pair

    # Calculate the high and low surrogates for symbols beyond BMP
    else:
        # Subtract 0x10000 from the symbol to get the 20-bit value
        symbol -= 0x10000

        # Calculate the high and low surrogates
        high_surrogate = 0xD800 | ((symbol >> 10) & 0x3FF)
        low_surrogate = 0xDC00 | (symbol & 0x3FF)

        return [high_surrogate, low_surrogate]


def show_surrogate():
    """
    Show surrogate pair
    """
    symbol = 0x1F602  # An emoji (outside BMP)
    surrogate_pair_list = surrogate_pair(symbol)
    print(f"Surrogate Pair for U+{symbol:04X}: {surrogate_pair_list}")


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
