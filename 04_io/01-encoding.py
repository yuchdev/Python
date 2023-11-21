import sys

__doc__ = """Show examples of debug print decorators.
From naive to production implementation.
"""


def text_to_bytes(text, encoding):
    try:
        # Encode the text using the specified encoding
        encoded_text = text.encode(encoding)

        # Convert the encoded bytes to a list
        bytes_list = list(encoded_text)

        return bytes_list
    except UnicodeEncodeError as e:
        # Handle encoding errors if necessary
        print(f"Error encoding the text: {e}")
        return []


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


def show_utf8():
    """
    Show how to convert text to bytes
    UTF-8 can't easily get n-th byte of character
    It's more compact than UTF-16
    """
    text = "Żółć"
    print(text_to_bytes(text, 'utf-8'))


def show_utf16():
    """
    Show how to convert text to bytes
    """
    text = "Żółć"
    print(text_to_bytes(text, 'utf-16'))


def show_utf32():
    """
    Show how to convert text to bytes
    """
    text = "Żółć"
    print(text_to_bytes(text, 'utf-32'))


def show_ascii():
    """
    Show how to convert text to bytes
    """
    text = "Hello World!"
    # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-3:
    # ordinal not in range(128)
    print(text_to_bytes(text, 'ascii'))


def show_ascii_exception():
    """
    Show how to convert text to bytes
    """
    text = "Żółć"
    # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-3:
    # ordinal not in range(128)
    print(text_to_bytes(text, 'ascii'))


def show_surrogate():
    """
    Show surrogate pair
    """
    symbol = 0x1F602  # An emoji (outside BMP)
    surrogate_pair_list = surrogate_pair(symbol)
    print(f"Surrogate Pair for U+{symbol:04X}: {surrogate_pair_list}")


def show_escape():
    """
    Show example of escape sequence
    """
    # 1. \x (Hexadecimal Escape Sequence):
    # One byte
    hex_escape = '\x41\x42\x43\x44\x45\x46'
    print(hex_escape)

    # 2. \u (Unicode Escape Sequence):
    # Two bytes
    unicode_escape = '\u0041\u0042\u0043\u0044\u0045\u0046'
    print(unicode_escape)

    # 3. \U (Unicode Escape Sequence):
    # Four bytes
    unicode_escape = '\U00000041\U00000042\U00000043\U00000044\U00000045\U00000046'
    print(unicode_escape)

    # 4. \N (Unicode Database ID Escape Sequence):
    # One or more bytes
    unicode_escape = '\N{GREEK CAPITAL LETTER DELTA}'
    print(unicode_escape)


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
