import sys
from collections import ChainMap

__doc__ = """ChainMap is a dictionary-like class for creating a single view of multiple mappings.
    ChainMap is a dictionary-like class for creating a single view of multiple mappings.
    Since it's view, all changes are reflected in the underlying mappings

"""

local_vars = {'a': 1, 'b': 2}
global_vars = {'c': 3, 'd': 4}
builtins = {'a': 5, 'f': 6}
cm = ChainMap(local_vars, global_vars, builtins)
# lookup is being performed from left to right
print(cm['a'])  # found in locals
print(cm['f'])  # found in builtins after checking in globals and locals
# notice 'a' is found in locals and not in builtins,
# but will be retrieved only from locals

# Get all mappings
for m in cm.maps:
    print(m)
