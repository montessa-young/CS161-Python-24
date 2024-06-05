# Review
name1 = "Mrs. Young"
# Variable - name 1
# = is called assignment
# "Mrs. Young" is a string

'''Multi line comments
can be done with 3 speech marks
at beginning and end'''
"""Works with single and 
double quotations"""


# Prompt for input
print("Enter a name")
name2 = input()
print("The name you entered is " + name2)
# input has to be assigned to a variable
# input() is expecting a string


# What about numbers?
print("Enter two numbers")
number1 = input()
number2 = input()
print(number1 + number2)
print(type(number1))
print(type(number2))

# There are other value types, Python guesses what type you want;
# int - integer
# float - floating decimal point
# bool - true or false

a = "5"
b = 5
c = 5.0
print("Variable a is type: ")
print(type(a))
print("Variable b is type: ")
print(type(b))
print("Variable c is type: ")
print(type(c))

# We can set input types to make them not strings.
print("Enter two numbers")
d = int(input())
f = int(input())
print(d + f)

# We can also convert variables to different types
e = int(a)
print(e)
print(type(e))

g = float(d)
h = float(f)
print(g + h)

# Bool is a True False and any input would be true.
print("Enter a number")
i = bool(input())
print(i)

# Input can be concatenated with dialog to input on the same line as output
j = input("Enter the name of a fruit")
print("The name you entered is: ", j)

