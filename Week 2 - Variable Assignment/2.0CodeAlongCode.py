# Speech marks - You can use '' or "" interchangeably - The choice between both types (single quotes and double quotes) depends on the programmer’s choice. Generally, double quotes are used for string representation and single quotes are used for regular expressions, dict keys or SQL. Hence both single quote and double quotes depict string in python but it’s sometimes our need to use one type over the other.

# Line below will create an error, so uncomment to demonstrate, then comment it back again.
# print('"It's Awesome")
# Correct code below
print('"It\'s Awesome"')


# Variables are mutable.
a = "Brooks"
a = "Igor"
a = "Mrs. Young"
print(a)


# Variable style
# all lower case no spaces is difficult to read
icantreadthisverywell = "confusing"
# camel case - used in JavaScript, TypeScript, and Java
iCanReadThisVeryWell = "better"
# snake case - used in Python
i_can_read_this_even_better = "This is what we will use"
# pascal case
ICanReadThis = "AndItsOnlyOneCharacterDifferentThanCamelCase"
# Screaming snake case - sometimes used to distinguish a variable that should be immutable.
NOW_WE_ARE_VERY_LOUD = "Don't change my value"
# kebab case - seen in URLs, uses dashes
#this-looks-like-kebab-case = "Like the BBQ skewer, but python thinks the dash might be a minus sign and doesn't like it."

print(i_can_read_this_even_better)
#print(i_can_raed_this_even_better)


# Concatenation - joining variables that represent strings
a = "Mrs. Young"
b = "excited"
c = "Friday"
print(a + "is" + b + "that it\'s" + c)
print(a + " is " + b + " that it\'s " + c)


import time
print("1st statement")
time.sleep(2)
print("2nd statement")