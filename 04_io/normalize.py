import sys
import unicodedata


def normalize(text, form='NFC'):
    """
    Normalize the string to decompose combined characters and remove non-ascii characters, e.g. 'é' -> 'e'
    :param text:
    :return: normalized string
    """
    normalized_string = unicodedata.normalize(form, text)
    return ''.join(c for c in normalized_string if ord(c) < 128)


def show_normalized():
    national_symbol_utf8 = "é"
    normalized_nkfd = normalize(national_symbol_utf8, 'NFKD')
    normalized_nfc = normalize(national_symbol_utf8, 'NFD')
    normalized_nfd = normalize(national_symbol_utf8, 'NFC')
    print(f"Original (UTF-8): {national_symbol_utf8}")
    print(f"NFKD Normalized (UTF-8): {normalized_nkfd}")
    print(f"NFC Normalized (UTF-8): {normalized_nfc}")
    print(f"NFD Normalized (UTF-8): {normalized_nfd}")


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
