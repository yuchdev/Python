from collections import OrderedDict

__doc__ = """The OrderedDict class provides all the same methods and operations 
as regular dictionaries (dict), but it also guarantees that the order 
in which you add items to the dictionary will be the order in which 
they are iterated over or retrieved. This can be particularly useful in scenarios
 where the order of elements matters
"""

ordered_dict = OrderedDict()

# Add key-value pairs in a specific order
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

# Iterate over the OrderedDict
for key, value in ordered_dict.items():
    print(key, value)

# Output will maintain the order:
# a 1
# b 2
# c 3
