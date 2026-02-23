# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# # Welcome to PPY lecture #2
#
# ## Introduction to object-oriented programming (OOP) and functional programming in Python

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Just a few organizational notes
#
# 1. Any questions from the last time?
# 2. Any problems with installing VSCode, git, uv, Python, or anything else?
# 3. Can you run the `git-pull.py` program to synchronize the content from GitLab on your computer?
#
# Feel free to discuss how to solve some problem with your friends or with me – that's one of the reasons why we come to the class 😊

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Object-oriented programming (OOP)
#
# ... is a programming paradigm that focuses on the creation of objects that contain both data and behavior. Python supports OOP and provides robust support for OOP concepts. Here are the main OOP concepts in Python and their uses:

# %% [markdown] slideshow={"slide_type": "fragment"}
# 1. Classes and Objects: A class is a blueprint for creating objects, while an object is an instance of a class. Classes define the properties and methods that all objects of that class will have. You can use classes and objects in Python to organize your code and create reusable code modules.

# %% [markdown] slideshow={"slide_type": "subslide"}
# 2. Inheritance: Inheritance is a way to create a new class based on an existing class. The new class inherits all the properties and methods of the existing class and can add new functionality or modify existing functionality. You can use inheritance in Python to reuse code and create new classes quickly.

# %% [markdown] slideshow={"slide_type": "subslide"}
# 3. Polymorphism: Polymorphism is the ability of objects of different classes to respond to the same message or method call. In Python, you can achieve polymorphism through method overloading and method overriding.

# %% [markdown] slideshow={"slide_type": "subslide"}
# 4. Encapsulation: Encapsulation is a way to hide the implementation details of a class from the outside world.

# %% [markdown] slideshow={"slide_type": "subslide"}
# An small example of how you can use OOP concepts in Python:

# %% slideshow={"slide_type": "fragment"}
# Define a class
class Car:
    def __init__(self, vendor, model, year):
        self.vendor = vendor
        self.model = model
        self.year = year

    def get_vendor(self):
        return self.vendor

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def __str__(self):
        return f"{self.vendor} {self.model} ({self.year})"

# Create an object of the class
car1 = Car("Toyota", "Corolla", 2018)

# Access properties and methods of the object
print(car1.get_vendor()) # Output: Toyota
print(car1.get_model()) # Output: Corolla
print(car1.get_year()) # Output: 2018
print(car1) # Output: Toyota Corolla (2018)

# %% [markdown] slideshow={"slide_type": "subslide"}
# In this example, we define a Car class with properties like make, model, and year, and methods like `get_vendor()`, `get_model()`, and `get_year()`. We also define a `__str__()` method to provide a string representation of the object. We then create an object of the class (car1) and access its properties and methods.

# %% [markdown] slideshow={"slide_type": "fragment"}
# For more details on basic OOP properties and examples, recall the class from 18ZPRO: [21 OOP (in Czech)](https://gitlab.fjfi.cvut.cz/ksi/zpro-2025-public/-/blob/main/21%20z%C3%A1klady%20OOP.ipynb) / [23 OOP (in English)](https://gitlab.fjfi.cvut.cz/ksi/zpro-2025-public-en/-/blob/main/23_introduction_to_OOP.ipynb?ref_type=heads)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### ... but "why"?
#
# It is not mandatory to use objects when programming in Python. For some reason, I have seen multiple situations of someone thinking that you are a better programmer if you follow the OOP principles. But IMHO it not always the case (we will get to an alternative approach later). 
#
# I am convinced that you will become a better programmer only if **you can choose the right tool for the task you are solving**. Let me show you one example where OOP helped me greatly.

# %% [markdown] slideshow={"slide_type": "subslide"}
# #### Advantages and disadvantages of OOP
#
# In Python, *everything is an object* – OOP is used heavily in the standard library and popular packages. Even if you do not write your own classes, you are essentially always a user of OOP.
#
# - ➕ OOP allows modeling systems using classes and objects, making it intuitive for domains like GUIs, games, or simulations where entities have state and behavior.
# - ➕ Inheritance enables code reuse – main functionality can be implemented in a base class and specific behavior can be implemented in derived classes.
# - ➕ Allows flexible and modular designs.
# - ➖ Risk of over-engineering. Simple problems are best addressed by simple constructs, such as plain functions.
# - ➖ Class hierarchies can be complex and hard to maintain.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Functional programming
#
# Focus: [functional programming](https://en.wikipedia.org/wiki/Functional_programming) in Python
# * lambda functions
# * `map()`
# * `filter()`
# * `reduce()`
# * `zip()`
# * iterools
# * decorator pattern

# %% [markdown] slideshow={"slide_type": "subslide"}
# ## Functional programming
#
# Functional programming is based on the idea of applying mathematical functions to data, where the function takes input arguments and produces an output value, without any side effects. In functional programming, the program flow is controlled by composing functions and passing data between them.
#
# The main advantage of functional programming over imperative programming is that it is often more declarative, concise, and easier to reason about. Functional programs are often easier to parallelize and more resilient to errors, as they don't rely on shared mutable state.
#
# Functional programming promotes immutability, where data cannot be changed after it's created. This can help avoid unintended side effects and make the code more predictable, which is crucial in data processing where maintaining data integrity is important.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Lambda functions
#
# Lambda functions are anonymous functions that can be defined inline without a name. They are commonly used in functional programming to create small, simple functions that can be passed as arguments to other functions.
#
# Lambda functions are useful when you need to define a simple function that is only used once and does not require a name, making your code more concise and readable.

# %% [markdown] slideshow={"slide_type": "subslide"}
# Syntax:
# ```
# lambda arguments: expression
# ```
#
# Here, arguments are the input parameters for the function, and expression is a single expression that the lambda function will evaluate. The result of the lambda function is the value of the expression.

# %% slideshow={"slide_type": "fragment"}
# example:
xyz = lambda x, y: x + y
result = xyz(5, 10)
print(result) # Output: 15

# %% [markdown] slideshow={"slide_type": "subslide"}
# Lambda functions can be used to define custom sorting orders for data structures like lists, tuples, and dictionaries. For example, to sort a list of tuples by the second element, you can use a lambda function as the key function for the `sorted()` function:

# %% slideshow={"slide_type": "fragment"}
my_list = [(2, 'b'), (1, 'c'), (3, 'a')]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list) # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


# %% slideshow={"slide_type": "fragment"}
def get_key(t):
    return t[0]

my_list = [(2, 'b'), (1, 'c'), (3, 'a')]
sorted_list = sorted(my_list, key=get_key)
print(sorted_list) # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Besides $\lambda$
#
# The `map()` function is used to apply a given function to each element of an iterable and return a new iterable with the results. The `filter()` function is used to create a new iterable by applying a given function to each element of an iterable and only including elements that satisfy a certain condition. The `reduce()` function is used to apply a given function to an iterable to reduce it to a single value.
#
# Lastly `zip()` is a built-in function in Python that is often used in functional programming to combine multiple lists into a single list of tuples. The zip() function takes two or more iterables as arguments and returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the iterables.

# %% [markdown] slideshow={"slide_type": "subslide"}
# For example... let's write code that takes a list of numbers as input and uses the `map()` function to create a new list that contains the square of each number in the original list.

# %% slideshow={"slide_type": "fragment"}
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares) # Output: [1, 4, 9, 16, 25]

# %% [markdown] slideshow={"slide_type": "subslide"}
# Write a code that takes a list of numbers as input and uses the `filter()` function to create a new list that only contains the even numbers in the original list.

# %% slideshow={"slide_type": "fragment"}
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) # Output: [2, 4]

# %% [markdown] slideshow={"slide_type": "subslide"}
# Write a code that takes a list of numbers as input and uses the `reduce()` function to calculate the product of all the numbers in the list.

# %% slideshow={"slide_type": "fragment"}
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x*y, numbers)
print(product) # Output: 120

# %% [markdown] slideshow={"slide_type": "subslide"}
# Last, but not least, these concepts are used eg. in list comprehension, which implements the logical principles of functional programming as well.

# %% [markdown] slideshow={"slide_type": "fragment"}
# An example of the `zip()` function:

# %% slideshow={"slide_type": "fragment"}
numbers = [1, 2, 3]
letters = ('a', 'c', 'b')
zipped = [f'{x[0]}/{x[1]}' for x in zip(numbers, letters)]
print(zipped) # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# %% [markdown] slideshow={"slide_type": "fragment"}
# ...we used `zip()` to combine the numbers list and the letters list into a list of tuples. This can be useful in many scenarios, such as when you need to iterate over two lists in parallel or when you want to create a dictionary from two lists.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Intro to `itertools`
#
# It is a built-in [module](https://docs.python.org/3/library/itertools.html), that should ...
#
# > [..] form an “iterator algebra” making it possible to construct specialized tools succinctly and efficiently in pure Python [..]
#
# Some notable functions in the `itertools` module are:
#
# 1. `count(start=0, step=1)` – Generates an infinite arithmetic progression starting from `start` with a step of `step`.
# 2. `cycle(iterable)` – Repeats the elements of the given iterable indefinitely.
# 3. `repeat(element, times=None)` – Repeats the specified `element` a specified number of `times` or indefinitely if `times` is not provided.
# 4. `chain(iterable1, iterable2, ...)` – Chains together multiple iterables into a single iterable.
# 5. `combinations(iterable, r)` – Generates all possible combinations of length `r` from the elements of the `iterable`.
# 6. `permutations(iterable, r=None)` – Generates all possible permutations of length `r` from the elements of the `iterable`.
# 7. `product(*iterables, repeat=1)` – Computes the Cartesian product of input iterables.
#
# See the [official Python documentation](https://docs.python.org/3/library/itertools.html) for details and examples how to use these functions 😊

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Contrast with OOP

# %% slideshow={"slide_type": "fragment"}
# Functional approach
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = list(filter(lambda x: x % 2 != 0, numbers))
squared_numbers = list(map(lambda x: x**2, filtered_numbers))


# %% slideshow={"slide_type": "subslide"}
class DataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_even(self):
        self.data = [x for x in self.data if x % 2 != 0]

    def square_numbers(self):
        self.data = [x**2 for x in self.data]

# Object-oriented approach
processor = DataProcessor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
processor.filter_even()
processor.square_numbers()


# %% [markdown] slideshow={"slide_type": "subslide"}
# The functional programming approach is more focused on the transformations applied to the data using functions, while the object-oriented programming approach encapsulates the operations within a class, emphasizing the state and behavior of an object. But **both approaches can be combined**.
#
# There is an interesting article on the topic topic of OOP vs functional programming: https://towardsdatascience.com/python-to-oop-or-to-fp-13ac79a43b16.

# %% [markdown]
# ## Decorator pattern, where function returns a function
#
# The decorator pattern in Python often involves defining a function that takes another function as input, modifies or enhances its behavior, and then returns a new function. This is achieved using the `@decorator` syntax in Python.
#
# For example:

# %%
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and keyword arguments {kwargs}.")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished execution with result: {result}.")
        return result
    return wrapper


# %% [markdown] slideshow={"slide_type": "fragment"}
# This decorator can be used to wrap any function as follows:

# %%
def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

decorated_add_numbers = log_function_call(add_numbers)
decorated_multiply_numbers = log_function_call(multiply_numbers)

# Calling the decorated functions
sum_result = decorated_add_numbers(3, 4)
product_result = decorated_multiply_numbers(b=5, a=2)


# %% [markdown] slideshow={"slide_type": "subslide"}
# But Python provides a *syntactic sugar* for using decorators directly in the *definition* of the decorated object:

# %%
@log_function_call
def add_numbers(a, b):
    return a + b

@log_function_call
def multiply_numbers(a, b):
    return a * b

# Calling the decorated functions
sum_result = add_numbers(3, 4)
product_result = multiply_numbers(b=5, a=2)

# %% [markdown]
# In this example, the `log_function_call` decorator adds logging statements before and after the execution of the decorated functions. When you call `add_numbers` or `multiply_numbers`, the decorator prints information about the function call and its result.
#
# This is useful because it allows you to **separate concerns** – the core functionality of adding or multiplying numbers is not cluttered with logging statements, yet you can easily add logging to any function you want without modifying its original code.
#
# Decorators are powerful tools for code organization and can be used for various purposes, such as memoization, caching, authentication, and more. They contribute to making code modular and more maintainable.

# %% [markdown]
# Further reading on decorators: https://realpython.com/primer-on-python-decorators/

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Data classes
#
# A **data class** in Python is a class that is primarily used to store and manage data. The [dataclasses](https://docs.python.org/3/library/dataclasses.html) module provides facilities to reduce *boilerplate code*.
#
# The main interface is the `@dataclass` decorator, which is most suitable for classes that define attributes with minimal logic:

# %% slideshow={"slide_type": "fragment"}
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self):
        return self.unit_price * self.quantity_on_hand

# %% [markdown] slideshow={"slide_type": "fragment"}
# The `@dataclass` decorator automatically adds, among other things, an `__init__()` function that looks like this (based on the class attributes):
#
# ```python
# def __init__(self, name, unit_price, quantity_on_hand = 0):
#     self.name = name
#     self.unit_price = unit_price
#     self.quantity_on_hand = quantity_on_hand
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Examples

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### 1. Classroom reservation system
#
# The assignment is in the [lectures/src/classroom_reservations/assignment.md](lectures/src/classroom_reservations/assignment.md) file.
# Create a `classroom_reservations` subfolder in the `exercises` folder, the sample solution will later appear in the `lectures/src/classroom_reservations` folder.
#
# What you will see:
#
# - How to design and use dataclasses for this problem
# - How to use the `ruff` extension in VSCode for code formatting and linting

# %% [markdown] slideshow={"slide_type": "subslide"}
# ### 2. Heuristics testing framework
#
# Let me walk you through [this implementation](https://github.com/matejmojzes/18heur-2020/tree/master/src).
