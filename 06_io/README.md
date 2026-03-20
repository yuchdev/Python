# Chapter 6. Input/Output

This chapter covers text encoding, filesystem operations, and advanced string formatting in Python.

## Text Encoding & Unicode
Python 3 uses Unicode for all strings. Understanding how text is represented as bytes is crucial for I/O.
* **Encodings**: ASCII (7-bit), UTF-8 (variable width, dominant on the web), UTF-16 (uses surrogate pairs for characters outside the Basic Multilingual Plane), and UTF-32 (fixed 4-byte).
* **Methods**: `text.encode(encoding)` converts str to bytes; `bytes.decode(encoding)` converts bytes to str.
* **Normalization**: `unicodedata.normalize(form, text)` handles canonical equivalence (e.g., `é` can be one code point or two). Common forms: `NFC`, `NFD`, `NFKC`, `NFKD`.
* **Escape Sequences**: `\xXX` (hex), `\uXXXX` (16-bit unicode), `\UXXXXXXXX` (32-bit unicode), `\N{name}` (Unicode database name).

## Filesystem API
Python's `open()` function is the primary interface for file I/O.
* **Modes**:
    * `r`: Read (default).
    * `w`: Write (overwrites).
    * `a`: Append.
    * `x`: Exclusive creation (fails if file exists).
    * `b`: Binary mode.
    * `t`: Text mode (default).
    * `+`: Open for updating (read and write).
* **Context Manager**: `with open(...) as f:` is the preferred way to handle files, ensuring they are closed even if an error occurs.
* **Pointer Manipulation**:
    * `tell()`: Returns the current stream position.
    * `seek(offset, whence)`: Changes the stream position. `whence` can be 0 (start), 1 (current), or 2 (end).
* **In-Memory Files**: `io.StringIO` and `io.BytesIO` allow you to treat strings and bytes as file-like objects.

## Advanced String Formatting
* **F-Strings**: `f"Value: {var:.2f}"` (Python 3.6+).
* **`format()` method**: `"{} {}".format(a, b)`.
* **Alignment & Padding**: `{:10}`, `{:>10}` (right), `{:^10}` (center), `{:*^10}` (padding with `*`).
* **Number Formatting**: Binary (`:b`), Hex (`:x`), Percentage (`:.2%`), Currency/Thousands separator (`:,`).

---
### Examples
* `01-encoding.py`: UTF-8/16/32 differences, surrogate pairs, and escape sequences.
* `02-surrogate.py`: Detailed look at surrogate pair calculation.
* `03-normalize.py`: Using `unicodedata` to normalize Unicode strings.
* `04-files.py`: File modes, `seek`, `tell`, and in-memory streams.
* `05-string.py`: Comprehensive guide to string methods and formatting.
