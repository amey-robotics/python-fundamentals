#Is the following variable name valid? Why?

#2name = "John"

"""
No, 2name = "John" is not a valid variable name in Python.

Why?

Variable names cannot start with a digit (0-9). Python's naming rules
require a variable name to begin with:

A letter (a-z, A-Z), or
An underscore (_)

Since 2name starts with the digit 2, 
Python will raise a syntax error.
"""

# Valid alternatives:

name2 = "John"
name_2 = "John"
_name = "John"