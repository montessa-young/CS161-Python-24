# Strings in Python

# We already know how to print a string, assign to a variable, and concatenate a string

print("Hello World")
x = "Hello Adrian"
y = 1
print("This is an example of concatenation. " + x)
print("This is another example of concatenating with an integer. Like number " + str(y) + ".")

# We can do multiline strings by using three double quotes or three single quotes

a = '''This is an example
of a multiple line
string.'''
print(a)

# Strings are Arrays (Lists) - so we can access the individual letters

print(x[1])

# We can loop through a string.
for letter in "bananas":
    print(letter)

# As we learned last week we can find the length of a string. It also counts spaces

print(len(x))

# We can check to see if a phrase or character in a string using the keyword in

phrase = "This is the best class ever"
if "best" in phrase:
    print("Yes, it is the best")

# Can also check if a phrase or character is not in the keyword using not in

if "good" not in phrase:
    print("what, you don't think its good")

# We can slice up strings, array starts at 0
y = "This is an amazing sentence"
print(y[8:18])

# Slice from the start
print(y[:8])

# Slice to the end
print(y[8:])

# Slice counting from the end
print(y[-13:-9])

# Upper case
print(y.upper())

# Lower case
print(y.lower())

# Title case
print(y.title())

# Remove leading and trailing spaces
m ="  this has spaces before and after  "
print(m.strip())

# Split a string
n = "This, is a good, example of, too many, commas"
print(n.split(","))

