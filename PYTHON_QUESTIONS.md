 Here are the **detailed answers** to all the **Core Python interview questions**:

---

## **1. Basic Types and Collections**
### **1. What are Python’s built-in data types? How do they differ?**
Python has several built-in data types:
- **Numeric types:** `int`, `float`, `complex`
- **Sequence types:** `list`, `tuple`, `range`, `str`
- **Set types:** `set`, `frozenset`
- **Mapping type:** `dict`
- **Boolean type:** `bool`
- **Binary types:** `bytes`, `bytearray`, `memoryview`

### **2. What is the difference between `is` and `==` in Python?**

- `==` checks for **value equality**.
- `is` checks for **identity** (whether two variables refer to the same object in memory).

Example:
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)  # True (same value)
print(a is c)  # False (different objects)
print(a is b)  # True (same object)
```

### **3. How does Python handle integer and floating-point precision?**
- Python integers (`int`) have arbitrary precision.
- Floating-point numbers (`float`) use **double-precision (64-bit)**, following IEEE 754.

Example:
```python
import sys
print(sys.float_info)  # Shows precision limits
```

### **4. What is the difference between a tuple and a list?**
- **Lists** are **mutable**, while **tuples** are **immutable**.
- **Tuples** are **faster** than lists.

### **5. What are the key differences between a set and a dictionary?**
- **Set** stores **unique unordered elements**.
- **Dictionary** stores **key-value pairs**.

Example:
```python
s = {1, 2, 3}
d = {"a": 1, "b": 2}
```

### **6. Explain how Python handles string immutability.**
- Strings in Python are **immutable**, meaning they cannot be modified in place.
- Every string operation that changes a string **creates a new object**.

### **7. What are list comprehensions?**
- They provide a concise way to create lists.

Example:
```python
squares = [x*x for x in range(10)]
```

### **8. How does dictionary key lookup work in Python?**
- Python dictionaries use **hash tables** to provide **O(1) average-time complexity** for lookups.

### **9. What are named tuples?**
- `collections.namedtuple` provides a **lightweight, immutable** alternative to dictionaries.

Example:
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
```

### **10. How do you merge two dictionaries efficiently?**
Python 3.9+:
```python
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2
```

---

## **2. Functions and Decorators**

### **11. What is the difference between `*args` and `**kwargs`?**
- `*args`: Allows passing **multiple positional arguments**.
- `**kwargs`: Allows passing **multiple keyword arguments**.

Example:
```python
def func(*args, **kwargs):
    print(args, kwargs)

func(1, 2, a=3, b=4)  # Output: (1, 2) {'a': 3, 'b': 4}
```

### **12. What is function caching (`functools.lru_cache`)?**
- Caches results of function calls to improve performance.

Example:
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

### **13. How do Python’s default mutable arguments behave unexpectedly?**
Mutable defaults **persist across function calls**.

Bad Example:
```python
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst
```
Fix:
```python
def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
```

### **14. What are first-class functions?**
- Functions can be **assigned to variables**, **passed as arguments**, and **returned** from other functions.

Example:
```python
def greet(name):
    return f"Hello, {name}"

g = greet
print(g("Alice"))
```

### **15. What are closures?**
- A function returning another function that captures variables.

Example:
```python
def outer(x):
    def inner(y):
        return x + y
    return inner
add_five = outer(5)
print(add_five(10))  # 15
```

### **16-20. Decorators & Partial Functions**
```python
from functools import wraps, partial

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(x, y):
    return x + y

print(add(3, 4))
```

---

## **3. Classes and OOP**

Here are **detailed answers** to the **Classes and OOP (21-30) questions** in Python.

---

## **21. What is the difference between class attributes and instance attributes?**
### **Class Attributes**  
- Shared **across all instances** of a class.  
- Defined directly in the class.  

### **Instance Attributes**  
- **Unique to each instance** of a class.  
- Defined inside the `__init__` method.

### **Example:**
```python
class Car:
    wheels = 4  # Class attribute

    def __init__(self, brand):
        self.brand = brand  # Instance attribute

car1 = Car("Toyota")
car2 = Car("Ford")

print(car1.wheels)  # 4 (shared)
print(car2.wheels)  # 4 (shared)
print(car1.brand)   # "Toyota" (unique)
print(car2.brand)   # "Ford" (unique)

Car.wheels = 6  # Modifying class attribute

print(car1.wheels)  # 6 (updated for all instances)
print(car2.wheels)  # 6 (updated for all instances)
```
---

## **22. What are Python’s special (`dunder`) methods?**
Special methods (also known as **magic methods**) start and end with `__` (double underscores). These methods allow **operator overloading** and custom behaviors.

### **Common `dunder` methods:**
- `__init__(self)`: Constructor  
- `__str__(self)`: Returns a user-friendly string representation  
- `__repr__(self)`: Returns a string for debugging  
- `__call__(self, *args)`: Makes an object callable  
- `__len__(self)`: Returns the length  

### **Example:**
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dog: {self.name}"  # Used for `print()`

    def __repr__(self):
        return f"Dog('{self.name}')"  # Used for debugging

    def __call__(self):
        return f"{self.name} is barking!"

dog = Dog("Buddy")
print(str(dog))  # Dog: Buddy
print(repr(dog)) # Dog('Buddy')
print(dog())     # Buddy is barking! (Callable object)
```
---

## **23. What is the difference between `staticmethod`, `classmethod`, and instance methods?**
### **1. Instance Methods (`self`)**
- Default method type.
- Operates on instance data.

### **2. Class Methods (`cls`)**
- Uses `@classmethod` decorator.
- Works with class attributes instead of instance attributes.

### **3. Static Methods (`@staticmethod`)**
- Uses `@staticmethod` decorator.
- No `self` or `cls` parameter.
- Independent utility function inside the class.

### **Example:**
```python
class MathOperations:
    base = 10

    def instance_method(self, x):
        return self.base + x  # Works with instance

    @classmethod
    def class_method(cls, x):
        return cls.base + x  # Works with class attribute

    @staticmethod
    def static_method(x, y):
        return x + y  # No dependency on instance or class

obj = MathOperations()
print(obj.instance_method(5))  # 15
print(MathOperations.class_method(5))  # 15
print(MathOperations.static_method(3, 4))  # 7
```
---

## **24. What is the difference between inheritance and composition?**
### **Inheritance (`is-a` Relationship)**
- A subclass inherits attributes and behaviors from a parent class.
- Useful for **hierarchical relationships**.

### **Composition (`has-a` Relationship)**
- A class contains objects of another class.
- More **flexible than inheritance**.

### **Example:**
```python
# Inheritance
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Dog "is-a" Animal
    def speak(self):
        return "Bark"

dog = Dog()
print(dog.speak())  # Bark

# Composition
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car "has-a" Engine

    def start(self):
        return self.engine.start()

car = Car()
print(car.start())  # Engine started
```
---

## **25. How does Python’s method resolution order (MRO) work?**
MRO determines **which method gets called** in case of **multiple inheritance**.  
Python follows the **C3 linearization (depth-first, left-to-right, avoiding repetition).**

### **Checking MRO:**
```python
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(A):
    def show(self):
        return "C"

class D(B, C):
    pass

print(D().show())  # B (left-most subclass method)
print(D.mro())  # [D, B, C, A, object]
```
---

## **26. What is the purpose of `super()`?**
- Calls the **parent class method** without explicitly naming the class.
- Useful in **multiple inheritance**.

### **Example:**
```python
class Parent:
    def show(self):
        return "Parent"

class Child(Parent):
    def show(self):
        return super().show() + " → Child"

print(Child().show())  # Parent → Child
```
---

## **27. What is metaprogramming in Python?**
Metaprogramming allows **creating or modifying classes dynamically**.

- **Metaclasses** define how **new classes** are created.
- `type()` can create classes at runtime.

### **Example:**
```python
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['new_method'] = lambda self: "Added dynamically"
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

obj = MyClass()
print(obj.new_method())  # "Added dynamically"
```
---

## **28. How can you make a Python class immutable?**
Using:
- **`__slots__`**
- **`property`**
- **Overriding `__setattr__`**  

### **Example with `__slots__`:**
```python
class ImmutableClass:
    __slots__ = ["name"]  # Restricts attribute creation

    def __init__(self, name):
        self.name = name

obj = ImmutableClass("Alice")
obj.name = "Bob"  # Works
obj.age = 25  # AttributeError
```
---

## **29. How do descriptors work in Python?**
A **descriptor** is an object that **manages attribute access** via `__get__`, `__set__`, `__delete__`.

### **Example:**
```python
class Descriptor:
    def __get__(self, instance, owner):
        return instance._value

    def __set__(self, instance, value):
        instance._value = value

class MyClass:
    attr = Descriptor()

    def __init__(self, value):
        self.attr = value

obj = MyClass(10)
print(obj.attr)  # 10
```
---

## **30. How do `__slots__` impact performance and memory usage?**
- **Reduces memory usage** by **preventing dynamic attribute creation**.
- **Improves attribute access speed**.

### **Example:**
```python
class WithSlots:
    __slots__ = ['x', 'y']  # Prevents dictionary overhead

class WithoutSlots:
    pass

import sys
a = WithSlots()
b = WithoutSlots()
print(sys.getsizeof(a))  # Smaller memory usage
print(sys.getsizeof(b))  # Larger memory usage due to __dict__
```

---

## **4. Exceptions and Error Handling**

Here are **detailed answers** for **Exceptions and Error Handling (31-40) questions** in Python:

---

## **31. What is the difference between `try-except` and `try-finally`?**
- `try-except`: **Handles** exceptions that may occur in the `try` block.
- `try-finally`: **Executes the `finally` block regardless of exceptions**, ensuring cleanup.

### **Example:**
```python
try:
    x = 1 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")  # Exception handled
finally:
    print("This will always execute.")  # Runs no matter what
```
**Output:**
```
Cannot divide by zero!
This will always execute.
```

---

## **32. How do custom exceptions work in Python?**
Custom exceptions are created by **subclassing `Exception`**.

### **Example:**
```python
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

def check_value(x):
    if x < 0:
        raise CustomError("Negative value not allowed!")

try:
    check_value(-5)
except CustomError as e:
    print(f"Error: {e}")
```
**Output:**
```
Error: Negative value not allowed!
```

---

## **33. How does Python’s exception handling affect performance?**
- **Exception handling is expensive** compared to normal flow.
- **Frequent exceptions slow down execution**.
- **Use exceptions for errors, not control flow**.

### **Bad Example (Using exceptions for flow control)**
```python
try:
    for i in range(1000000):
        raise ValueError  # Unnecessary exception
except ValueError:
    pass
```
💡 **Fix:** Use an `if` condition instead of raising exceptions unnecessarily.

---

## **34. What happens if an exception occurs inside a generator?**
- If an exception occurs in a generator, it **terminates immediately**.
- The exception **propagates to the caller**.

### **Example:**
```python
def my_generator():
    yield 1
    raise ValueError("Generator error!")
    yield 2  # This will never execute

g = my_generator()
print(next(g))  # Output: 1
print(next(g))  # Raises ValueError
```
---

## **35. What are context managers, and how do they help with exception handling?**
Context managers simplify **resource management** (e.g., file handling, database connections).

💡 **They automatically close resources** even if an error occurs.

### **Example (File Handling)**
```python
with open("file.txt", "w") as f:
    f.write("Hello, World!")  # File is automatically closed
```
Without `with`, you’d have to manually call `f.close()`.

---

## **36. How do you create a custom context manager using `__enter__` and `__exit__`?**
A class can define:
- `__enter__()`: Setup logic (e.g., open a file).
- `__exit__()`: Cleanup logic (e.g., close the file).

### **Example:**
```python
class MyContext:
    def __enter__(self):
        print("Entering...")
        return self  # Returned object is available in 'as' variable

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting...")

with MyContext() as obj:
    print("Inside context")

# Output:
# Entering...
# Inside context
# Exiting...
```

---

## **37. How does Python’s `with` statement work internally?**
When you use `with`, Python:
1. Calls **`__enter__()`** on the context manager.
2. Executes the block inside `with`.
3. Calls **`__exit__()`**, ensuring cleanup.

It is equivalent to:
```python
ctx = MyContext()
ctx.__enter__()
try:
    print("Inside context")
finally:
    ctx.__exit__(None, None, None)
```
---

## **38. What is the `raise from` syntax in Python?**
Used to **chain exceptions** while maintaining the original traceback.

### **Example:**
```python
try:
    raise ValueError("Original error")
except ValueError as e:
    raise RuntimeError("New error") from e
```
This keeps a **reference to the original exception**, useful for debugging.

**Without `from`:**
```python
raise RuntimeError("New error")
```
The original error’s traceback is lost.

---

## **39. How can you log exceptions without stopping program execution?**
Use **`logging`** instead of `print()` for better debugging.

### **Example:**
```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    x = 1 / 0
except ZeroDivisionError as e:
    logging.error("An error occurred", exc_info=True)  # Logs exception details
```
**Output:**
```
ERROR:root:An error occurred
Traceback (most recent call last):
  File "example.py", line 5, in <module>
    x = 1 / 0
ZeroDivisionError: division by zero
```
---

## **40. What is `sys.exc_info()` and how is it used for debugging?**
- `sys.exc_info()` returns **(exception type, exception value, traceback)**.
- Used when handling exceptions in **custom logging**.

### **Example:**
```python
import sys

try:
    1 / 0
except ZeroDivisionError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"Type: {exc_type}")  # Type: <class 'ZeroDivisionError'>
    print(f"Message: {exc_value}")  # Message: division by zero
```

---

### **Summary of Key Takeaways**
| **Question** | **Key Concept** |
|-------------|----------------|
| `try-except` vs `try-finally` | `finally` always executes for cleanup |
| Custom exceptions | Create by subclassing `Exception` |
| Exception performance | Avoid exceptions in loops |
| Generator exceptions | Stop iteration and propagate |
| Context managers | Use `with` for auto-cleanup |
| Custom context managers | Define `__enter__` and `__exit__` |
| `with` statement internals | Calls `__enter__()`, executes block, then `__exit__()` |
| `raise from` | Maintains original traceback |
| Logging exceptions | Use `logging.error(exc_info=True)` |
| `sys.exc_info()` | Provides exception type, value, traceback |

---

## **5. Async Programming**

### **41. What is the difference between threading and multiprocessing in Python?**
- **Threading:** Runs multiple threads within the same process. Each thread shares memory but is limited by the **Global Interpreter Lock (GIL)**. Useful for **I/O-bound tasks** (networking, file I/O).
- **Multiprocessing:** Runs separate processes, each with its own memory space, bypassing the GIL. Useful for **CPU-bound tasks** (image processing, mathematical computations).

Example:
```python
import threading, multiprocessing

def worker():
    print("Working...")

# Threading
t = threading.Thread(target=worker)
t.start()
t.join()

# Multiprocessing
p = multiprocessing.Process(target=worker)
p.start()
p.join()
```

---

### **42. What is Python’s Global Interpreter Lock (GIL), and how does it affect multithreading?**
- The **GIL** allows only one thread to execute Python bytecode at a time, preventing true parallel execution in CPU-bound tasks.
- **I/O-bound tasks** benefit from threading since the GIL is released during I/O operations.
- **Multiprocessing** is recommended for CPU-bound tasks as it avoids the GIL.

Example (I/O-bound task benefits from threading):
```python
import threading
import time

def io_task():
    time.sleep(2)
    print("Task complete")

t1 = threading.Thread(target=io_task)
t2 = threading.Thread(target=io_task)

t1.start()
t2.start()
t1.join()
t2.join()
```

---

### **43. How does `asyncio` work in Python?**
- `asyncio` enables **asynchronous (non-blocking) execution** using a **single-threaded event loop**.
- It operates using **coroutines**, which pause execution (`await`) until the awaited operation is complete.
- Unlike **threading**, `asyncio` does not rely on multiple OS threads.

Example:
```python
import asyncio

async def async_task():
    print("Start task")
    await asyncio.sleep(2)  # Non-blocking sleep
    print("Task complete")

asyncio.run(async_task())
```

---

### **44. What is the difference between `async` functions and normal functions?**
- **Normal functions** execute sequentially and return values immediately.
- **`async` functions return coroutines**, which need to be awaited for execution.

Example:
```python
import asyncio

async def async_function():
    return "Hello, Async!"

result = async_function()  # Returns a coroutine, NOT "Hello, Async!"
print(result)  # <coroutine object async_function at ...>

# Correct way:
print(asyncio.run(async_function()))  # "Hello, Async!"
```

---

### **45. How does `await` work, and what can you `await` in Python?**
- `await` pauses the execution of an `async` function until the awaited coroutine completes.
- You can `await`:
  - Another coroutine
  - An `asyncio.Future` object
  - Some third-party async libraries (e.g., `httpx`, `aiomysql`)

Example:
```python
import asyncio

async def delay():
    await asyncio.sleep(2)
    return "Done"

async def main():
    result = await delay()  # Waits for `delay()` to finish
    print(result)

asyncio.run(main())
```

---

### **46. What are `asyncio.gather()` and `asyncio.create_task()` used for?**
- `asyncio.gather()` runs multiple coroutines concurrently and returns results.
- `asyncio.create_task()` schedules a coroutine but does not wait for it.

Example:
```python
import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    return f"Task {name} finished"

async def main():
    result = await asyncio.gather(task("A", 2), task("B", 1))
    print(result)

asyncio.run(main())  # ['Task A finished', 'Task B finished']
```

Example using `asyncio.create_task()`:
```python
async def independent_task():
    await asyncio.sleep(1)
    print("Task completed")

async def main():
    asyncio.create_task(independent_task())  # Task runs in the background
    print("Main function running")
    await asyncio.sleep(2)  # Ensure the event loop is running

asyncio.run(main())
```

---

### **47. How does `asyncio.run()` simplify running event loops?**
- `asyncio.run()` **creates, runs, and closes** an event loop.
- You cannot use `asyncio.run()` **inside an existing event loop** (e.g., Jupyter Notebook).

Example:
```python
import asyncio

async def hello():
    print("Hello, asyncio!")

asyncio.run(hello())  # Proper way to run an async function
```

💡 **Inside an existing event loop (e.g., Jupyter Notebook), use `await hello()` instead.**

---

### **48. How do you mix `async` and `sync` code correctly?**
- Blocking operations inside `async` functions should be **offloaded** using `asyncio.to_thread()`.
- Running an `async` function inside a synchronous function requires `asyncio.run()`.

Example (running sync inside async):
```python
import asyncio

import time

def blocking_function():
    time.sleep(2)
    return "Done"

async def main():
    result = await asyncio.to_thread(blocking_function)  # Runs blocking_function in a separate thread
    print(result)

asyncio.run(main())
```

Example (running async inside sync):
```python
async def async_function():
    return "Hello from async"

def sync_function():
    result = asyncio.run(async_function())  # Correct way to call async function
    print(result)

sync_function()
```

---

### **49. How do you handle exceptions inside async coroutines?**
- Use **`try-except` inside async functions**.
- If using `asyncio.gather()`, pass `return_exceptions=True` to avoid task cancellation.

Example (handling exception inside coroutine):
```python
import asyncio

async def error_task():
    raise ValueError("Something went wrong")

async def main():
    try:
        await error_task()
    except ValueError as e:
        print(f"Handled error: {e}")

asyncio.run(main())
```

Example (handling exceptions in `asyncio.gather()`):
```python
async def faulty_task():
    raise ValueError("Error!")

async def safe_task():
    return "Success"

async def main():
    results = await asyncio.gather(faulty_task(), safe_task(), return_exceptions=True)
    print(results)  # Output: [ValueError('Error!'), 'Success']

asyncio.run(main())
```

---

### **50. What are `asyncio.Semaphore` and `asyncio.Lock`, and why are they useful?**
- **`asyncio.Lock()`** ensures that **only one coroutine accesses** a shared resource at a time.
- **`asyncio.Semaphore(N)`** allows **up to `N` coroutines** to access a shared resource **concurrently**.

Example using `asyncio.Lock()`:
```python
import asyncio

lock = asyncio.Lock()

async def protected_task(name):
    async with lock:  # Ensures only one task enters at a time
        print(f"{name} is using the resource")
        await asyncio.sleep(2)
        print(f"{name} released the resource")

async def main():
    await asyncio.gather(protected_task("Task A"), protected_task("Task B"))

asyncio.run(main())
```

Example using `asyncio.Semaphore()`:
```python
sem = asyncio.Semaphore(2)  # Allows 2 concurrent tasks

async def limited_task(name):
    async with sem:  # Ensures only 2 tasks run at the same time
        print(f"{name} is running")
        await asyncio.sleep(2)

async def main():
    await asyncio.gather(limited_task("Task A"), limited_task("Task B"), limited_task("Task C"))

asyncio.run(main())
```

---

## **6. Performance Optimization**

## **Performance Optimization in Python (Detailed Answers: 51-60)**  

Here are deeply detailed explanations with examples for **Performance Optimization (51-60) in Python**.

---

### **51. How does Python manage memory allocation? What are reference counting and garbage collection?**
Python uses **automatic memory management** via **reference counting** and **garbage collection**.

#### **Reference Counting**
- Every object in Python has a **reference count**.
- When the reference count reaches **zero**, the object is deallocated.

Example:
```python
import sys

a = [1, 2, 3]
print(sys.getrefcount(a))  # Output: Reference count of `a`
b = a
print(sys.getrefcount(a))  # Increased reference count
del b
print(sys.getrefcount(a))  # Decreased again
```

#### **Garbage Collection (GC)**
- Python’s **GC removes cyclic references**.
- Uses **generational garbage collection** to optimize cleanup.

Manually running garbage collection:
```python
import gc
gc.collect()  # Forces garbage collection
```
💡 **Performance Tip:** **Avoid cyclic references** (`self.a = self` inside classes) to minimize GC overhead.

---

### **52. What are Python’s `__slots__`, and how do they improve performance?**
- By default, Python stores object attributes in a **dictionary (`__dict__`)**.
- Using `__slots__` prevents this dictionary creation, reducing memory usage.

#### **Example:**
```python
class WithSlots:
    __slots__ = ['x', 'y']  # Limits instance attributes

    def __init__(self, x, y):
        self.x = x
        self.y = y

class WithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

import sys
a = WithSlots(1, 2)
b = WithoutSlots(1, 2)

print(sys.getsizeof(a))  # Uses less memory
print(sys.getsizeof(b))  # Uses more memory
```
✅ **Use `__slots__` in memory-constrained applications** (e.g., embedded systems).

---

### **53. How do you profile Python code for performance bottlenecks?**
**Profiling** helps identify slow parts of your code.

#### **Using `cProfile` (Recommended for CPU profiling)**
```bash
python -m cProfile my_script.py
```
OR:
```python
import cProfile
cProfile.run("my_function()")
```

#### **Using `timeit` for micro-benchmarks**
```python
import timeit
print(timeit.timeit("sum(range(100))", number=1000000))
```

#### **Using `line_profiler` for per-line performance profiling**
```bash
pip install line-profiler
```
```python
from line_profiler import LineProfiler

def my_function():
    total = 0
    for i in range(10000):
        total += i
    return total

lp = LineProfiler()
lp.add_function(my_function)
lp.enable_by_count()
my_function()
lp.print_stats()
```
✅ **Best Practice:** Use **`cProfile`** for **high-level analysis** and **`line_profiler`** for **fine-grained details**.

---

### **54. What is the difference between `deepcopy()` and `copy()` in Python?**
- **`copy.copy()`** → **Shallow copy** (copies references, not objects).
- **`copy.deepcopy()`** → **Deep copy** (recursively copies all objects).

#### **Example:**
```python
import copy

a = [[1, 2], [3, 4]]
shallow = copy.copy(a)
deep = copy.deepcopy(a)

a[0][0] = 99
print(shallow)  # [[99, 2], [3, 4]] (references updated)
print(deep)     # [[1, 2], [3, 4]] (remains unchanged)
```
✅ **Use `deepcopy()` when modifying nested structures**.

---

### **55. How does NumPy achieve better performance than Python lists?**
**NumPy** is faster because:
- Uses **contiguous memory allocation**.
- Uses **vectorized operations** in C.
- Supports **SIMD (Single Instruction, Multiple Data)** optimizations.

#### **Example:**
```python
import numpy as np
import time

lst = list(range(1000000))
arr = np.array(lst)

start = time.time()
sum(lst)  # Python list sum
print("List Sum:", time.time() - start)

start = time.time()
np.sum(arr)  # NumPy sum (much faster)
print("NumPy Sum:", time.time() - start)
```
✅ **Use NumPy for numerical and matrix operations**.

---

### **56. What is Just-In-Time (JIT) compilation, and does Python support it?**
- **JIT** compiles code at runtime for **faster execution**.
- **Python (CPython) doesn’t have JIT**, but **PyPy** provides **JIT optimizations**.

#### **Example:**
Using **PyPy** (instead of CPython):
```bash
pypy my_script.py
```
✅ **Use PyPy for CPU-bound Python applications**.

---

### **57. What is the purpose of `Cython`, and how does it improve performance?**
- **Cython** compiles Python code to **C for speed**.
- Works well for **CPU-intensive tasks**.

#### **Example:**
1. Install Cython:
```bash
pip install cython
```
2. Create a `speedup.pyx` file:
```cython
def add(int a, int b):
    return a + b
```
3. Compile it:
```bash
cythonize -i speedup.pyx
```
4. Use it in Python:
```python
import speedup
print(speedup.add(10, 20))
```
✅ **Use Cython for performance-critical code**.

---

### **58. How does `multiprocessing.Pool` improve CPU-bound task performance?**
- **`Pool`** distributes tasks across multiple **processes**, bypassing the GIL.

#### **Example:**
```python
from multiprocessing import Pool

def square(x):
    return x * x

with Pool(4) as p:
    results = p.map(square, [1, 2, 3, 4])
print(results)  # [1, 4, 9, 16]
```
✅ **Use `Pool` for CPU-heavy tasks**.

---

### **59. How does `functools.lru_cache` improve performance?**
- **Caches function calls** to avoid recomputation.
- Best for **expensive recursive functions**.

#### **Example:**
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(50))  # Cached for better performance
```
✅ **Use `lru_cache` for expensive recursive calls**.

---

### **60. How does `memoryview` help with optimizing performance in Python?**
- **Avoids copying data** when slicing large binary objects.
- Works on `bytes`, `bytearray`, and `array.array`.

#### **Example:**
```python
data = bytearray(b"Hello World")
view = memoryview(data)
view[:5] = b"HELLO"
print(data)  # b'HELLO World'
```
✅ **Use `memoryview` for large binary data manipulation**.

---

### **Final Takeaways:**
| **Optimization Technique** | **Benefit** |
|----------------------------|-------------|
| `__slots__` | Reduces memory usage |
| `cProfile`, `line_profiler` | Identifies performance bottlenecks |
| `deepcopy()` vs `copy()` | Avoids unintended modifications |
| NumPy | Fast array operations |
| PyPy | JIT for better performance |
| Cython | Compiles Python to C |
| `multiprocessing.Pool()` | Bypasses GIL for CPU tasks |
| `lru_cache` | Speeds up recursive calls |
| `memoryview` | Optimizes binary data handling |
