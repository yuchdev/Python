import pdb

__doc__ = """The Python Debugger (PDB) is a built-in interactive debugger 
that allows you to set breakpoints in your code, inspect variables, 
and step through your code line by line to diagnose and debug issues

pdb.set_trace() enters debugger interactive mode.
In the PDB interactive mode, you can use various commands to inspect and control the program. 
Some common commands include:

* c (continue): Resume program execution
* n (next): Execute the current line and move to the next line
* s (step): Execute the current line and enter functions called in that line
* q (quit): Exit the debugger and terminate the program
* p <variable> (print): Print the value of a variable
* list: Show the source code around the current line
* h (help): Show a list of available commands
* u (up) and d (down): Move up and down the call stack
"""


def some_function():
    """
    When you run your script, it will execute until it encounters the pdb.set_trace() line.
    At that point, the program will pause, and you'll be in the debugger interactive mode.
    You will see function signature and the line of code that will be executed next.
    You can inspect the values of x and y and then continue program execution with the c command
    E.g.
    > python 06-pdb.py
    > 06-pdb.py(42)some_function()
    -> return result
    (Pdb) p x
    10
    (Pdb) p y
    5
    (Pdb) c
    """
    x = 10
    y = 5
    result = x / y
    # This sets a breakpoint
    pdb.set_trace()
    return result


# Launch the debugger
some_function()
