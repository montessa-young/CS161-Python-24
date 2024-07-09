# The Python interpreter has a number of functions and types built into it that are always available. We are going to review the ones we already know and then learn more.

# We already know these (or should):
a = 1
b = 2
c = 100.23
d = 134

bool(a)
print(a)
float(b)
print(b)
int(c)
print(c)
str(d)
print("This number can now be concatenated " + str(d))
print(type(d))
input("Input a number")

# Here are the new ones:
e = -99
abs(e)
print(e)
# returns the absolute value of a number
example_list = [3, 2, 4, 5, 6, 89]
print(len(example_list))
# returns the length(the number of items) of an object. Works on strings, list, and range.

print(max(example_list))
# return the largest item in an iterable or the largest of two or more arguments.

print(min(example_list))
# return the smallest item in an iterable or the smallest of two or more arguments.

print(pow(8,4))
# return base to the power exponential.

print(round(1.456, 2))
# return number rounded to ndigits precision after the decimal point. If ndigits is omitted or is None, it returns the nearest integer to its input.

print(sum(example_list))
# return sums start and the items of an iterable from left to right and returns the total. The iterable’s items are normally numbers, and the start value is not allowed to be a string.

print(dir(1))
# returns information about any value and tells you the functions that are available to use in alphabetical order


# import
# import libraries that offer other built-in functions

import time
time.sleep(3)
time.process_time()

import random
random.randint(1,100)
random.shuffle(example_list)
print(example_list)

help()
# invokes the built-in help system