import sys

__doc__ = """Philosophy and theory of exceptions and error handling
Exception handling in Python is quite simple, based of try-except-finally for handling,
raise is used to raise an exception
Process of exception handling includes stack unwinding, which is the process of
removing one layer of function call from the call stack

Let's talk about error handling in general, not only in Python:
* 92% of catastrophic errors in complex systems are due to wrong error handling
* error handling is more complex than handling of normal cases
* testing of error handling is more difficult than testing of normal cases
* error handling is often not tested at all

There are 2 interesting techniques for error handling:
* make as many error case impossible or make them normal cases (e.g. restore db from backup every day)
* crash-only software: if something goes wrong, crash the system and restart it

What could be considered as an error?
* Errors due to wrong input or other runtime errors
* Errors due to wrong usage of the system
* Errors due to system failures
* Error due to communication failures

Example: opening file with CLI argument could end up an error if the file does not exist
However, in GUI application, the user should be notified about the error and asked to select another file

Interesting approach of handling is to exclude except blocks and use only try-finally blocks (see example below)

During stack unwinding we go further from the place where the exception was raised
Thus we are losing information about the context of the exception
Conclusion: handle exceptions as close to the place where they were raised as possible

The only way where you can catch all exceptions arbitrary far away from the place 
where they were raised is an attempt to keep the system running or keep system consistency

There are 3 levels of exception safety (came from C++):
* No-throw guarantee: no exceptions are thrown
* Strong exception safety: if an exception is thrown, the program state is the same as before the operation
* Basic exception safety: if an exception is thrown, the program state is valid, 
  but not necessarily the same as before the operation
  
Possible exception boundaries:
* User input
* Thread
* Process
* Machine

Logging and Debugging:
* Python's logging module is helpful for logging error messages and debugging information
* The pdb module provides a built-in debugger for tracing errors and debugging code interactively
"""

# Exception handling in Python is quite simple, based of try-except-finally for handling,
# raise is used to raise an exception
try:
    print(f"This is the try block 1 / 0={1 / 0}")
except ZeroDivisionError:
    print("You cannot divide by zero")
    raise
finally:
    print("This will always be executed")


# One more approach is to exclude except blocks and use only try-finally blocks
print("setup_resources()")
try:
    print("do_something()")
finally:
    print("cleanup_resources()")
