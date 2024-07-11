# String Methods in Python

# All string methods return new values. They do not change the original string.

string_example = "This is an example of a string."
print(string_example.title())
print(string_example)

# To change an actual string you need to assign the method to a new variable.
string_changed = string_example.title()
print(string_changed)

# MORE FORMATTING
# Capitalize (just the first letter of the first word in the string)
string1 = "mrs. Young"
print(string1.capitalize())

# Casefold or lower - Converts string into lower case, same as .lower
string2 = "THIS IS CAPITALIZED"
print(string2.casefold())
print(string2.lower())

# Swapcase - Switches from lower case to upper case and vice versa
string3 = "THIS is NOT capitalized"
print(string3.swapcase())

# Format - formats a specified value and inserts them inside the string's placeholder
string4 = "For only {price:.2f} dollars, you can buy this book!"
print(string4.format(price = 29.999))
string5 = "For only {price:,.2f} dollars, you can buy this book!"
print(string5.format(price = 45678))
string6 = "Today only, this is {discount:%} off!"
print(string6.format(discount = .60))
string7 = "My name is {fname}, I'm {age} years old."
print(string7.format(fname = "John", age = 35))

# Is the entry correct? Checkers that return True
#isalpha()	Returns True if all characters in the string are in the alphabet
string8 = "This is a string with letters"
string9 = "Thishasnospaces"
print(string8.isalpha())
print(string9.isalpha())
#isalnum()	Returns True if all characters in the string are alphanumeric
string10 = "1234abcd"
print(string10.isalnum())
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
string11 = "1234"
print(string11.isdecimal())
string12 = "1234"
print(string12.isdigit())

#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case

# Joining Strings in a list back to a single string with a separator

wordlist = ["Mary", "Maggie", "Mike"]
separator = " "
print(separator.join(wordlist))

wordstring = separator.join(wordlist)
print(wordstring)