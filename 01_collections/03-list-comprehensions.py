import os
import sys
import glob
import random
import timeit


def create():

    # A list comprehension provides a compact way of mapping a list into another list by applying a function
    a_list = [1, 2, 3, 4]
    print("a_list={}".format(a_list))
    a_list2 = [elem * 2 for elem in a_list]
    print("[elem*2 for elem in a_list]={0}".format(a_list2))

    # another example
    names = ['Elwood', 'Jake']
    print("names={}".format(names))
    names2 = [name.lower() for name in names]
    print("[name.lower() for name in names]={}".format(names2))


def files():
    # it does not change the original list
    files_in_dir = [os.path.realpath(f) for f in glob.glob('*.py')]
    print("[os.path.realpath(f) for f in glob.glob('*.py')]={}".format(files_in_dir))

    # List comprehensions can also filter items
    big_in_dir = [os.path.realpath(f) for f in glob.glob('*.py') if os.stat(f).st_size > 600]
    print("[os.path.realpath(f) for f in glob.glob('*.py') if os.stat(f).st_size > 600]={}".format(big_in_dir))

    # there’s no limit to how complex a list comprehension can be
    sizes = [(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py')]
    print("[(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py')]={}".format(sizes))


def queries():
    stocks = [
        {'price': 91.10, 'name': 'IBM', 'shares': 50},
        {'price': 83.44, 'name': 'CAT', 'shares': 150},
        {'price': 51.23, 'name': 'MSFT', 'shares': 200},
        {'price': 40.37, 'name': 'GE', 'shares': 95},
        {'price': 65.10, 'name': 'MSFT', 'shares': 50},
        {'price': 70.44, 'name': 'IBM', 'shares': 100}
    ]
    print("stocks={}".format(stocks))

    stocknames = [s['name'] for s in stocks]
    print("[s['name'] for s in stocks]={}".format(stocknames))

    # You can perform database-like queries on sequences
    query = [s for s in stocks if s['price'] > 50.0 and s['shares'] > 100]
    print("[s for s in stocks if s['price'] > 50.0 and s['shares'] > 100]={}".format(query))

    query = [s for s in stocks if s['name'] in ('MSFT', 'IBM')]
    print("[s for s in stocks if s['name'] in ('MSFT', 'IBM')]={}".format(query))

    # combine a list comprehension with a sequence reduction
    cost = sum([s['shares'] * s['price'] for s in stocks])
    print("sum([s['shares'] * s['price'] for s in stocks])={}".format(cost))


def walrus():
    # walrus operator allows you to run an expression
    # while simultaneously assigning the output value to a variable
    def get_weather_data():
        """
        :return: current random weather from 22 to 32
        """
        return random.randrange(22, 32)

    temperature = list(random.sample(range(0, 30), 5))
    print("temperature = {}".format(temperature))
    hot_temps = [temp for _ in temperature if (temp := get_weather_data()) >= 25]
    print("[temp for _ in range(20) if (temp := get_weather_data()) >= 25]={}".format(hot_temps))


def matrix():
    matrix1 = [[i for i in range(5)] for _ in range(5)]
    print("[[i for i in range(5)] for _ in range(5)]")
    print(matrix1)


def performance():
    """
    A list comprehension in Python works by loading the entire output list into memory
    it’s often helpful to use a generator instead of a list comprehension in Python
    A generator doesn't create a single, large data structure in memory, but instead returns an iterable
    """
    # You can tell this is a generator because the expression isn’t surrounded
    # by brackets or curly braces. Optionally, generators can be surrounded by parentheses
    ret = sum(i * i for i in range(1000000))
    print("sum(i * i for i in range(1000000))={}".format(ret))


def measure():
    """
    Compare to comprehension:
    timeit is a useful library for timing how long it takes chunks of code to run
    E.g. loop take 50% longer to execute than comprehension
    """
    print("Elapsed: {}".format(timeit.timeit(performance, number=10)))


# Some examples from Codewars
def descending_order(num):
    """
    Your task is to make a function that can take any non-negative integer as an argument
    and return it with its digits in descending order
    """
    return int("".join(sorted(str(num), reverse=True)))


def high_and_low(numbers):
    """
    In this little assignment you are given a string of space separated numbers,
    and have to return the highest and lowest number.
    """
    return "{} {}".format(max(numbers.split(" ")), min(numbers.split(" ")))


def find_short(s):
    """
    Simple, given a string of words, return the length of the shortest word(s).
    String will never be empty and you do not need to account for different data types.
    """
    return min([len(i) for i in s.split(" ")])


def to_camel_case(text):
    """
    Complete the method/function so that it converts dash/underscore delimited words into camel casing.
    The first word within the output should be capitalized only if the original word was capitalized
    (known as Upper Camel Case, also often referred to as Pascal case).
    """
    return "".join([i.capitalize() for i in text.replace("-", "_").split("_") if i != text[0]])


def no_vowel(string_):
    """
    Trolls are attacking your comment section!
    A common way to deal with this situation is to remove all of the vowels from the trolls' comments,
    neutralizing the threat.
    Your task is to write a function that takes a string and return a new string with all vowels removed.
    For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
    """
    return "".join([i for i in string_ if i.lower() not in "aeiou"])


def persistence(n):
    """
    Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
    which is the number of times you must multiply the digits in num until you reach a single digit.
    """
    count = 0
    while len(str(n)) > 1:
        n = eval("*".join(str(n)))
        count += 1
    return count


def row_sum_odd_numbers(n):
    """
    Given the triangle of consecutive odd numbers:
    Calculate the row sums of this triangle from the row index (starting at index 1)
    """
    return n ** 3


def find_uniq(arr):
    """
    There is an array with some numbers
    All numbers are equal except for one. Try to find it!
    It’s guaranteed that array contains at least 3 numbers.
    The tests contain some very huge arrays, so think about performance.
    """
    return [i for i in set(arr) if arr.count(i) == 1][0]


def is_pangram(s):
    """
    A pangram is a sentence that contains every single letter of the alphabet at least once.
    For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
    because it uses the letters A-Z at least once (case is irrelevant).
    Given a string, detect whether or not it is a pangram.
    Return True if it is, False if not. Ignore numbers and punctuation.
    """
    return len(set([ltr.lower() for ltr in s if ltr.isalpha()])) == 26


def unique_in_order(sequence):
    """
    Implement the function unique_in_order which takes as argument a sequence
    and returns a list of items without any elements with the same value next to each other
    and preserving the original order of elements.
    For example:
    unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
    unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
    """
    if len(sequence) == 0:
        return []
    return [sequence[i] for i in range(len(sequence)) if i == 0 or sequence[i] != sequence[i - 1]]



if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")

