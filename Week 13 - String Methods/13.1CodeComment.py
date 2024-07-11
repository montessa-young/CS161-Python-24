string1 = "mrs. young"
print(string1.capitalize())
#


string2 = "THIS is a sentence"
print(string2.casefold())
#

string3 = "THIS is another EXAMPLE sentence"
print(string3.swapcase())
#

string4 = "For only {price:.2f} dollars, you can buy this toy!"
print(string4.format(price=30.145))
#


string8 = "This is a string with letters"
string9 = "Thishasnospaces"
string10 = "12345abcd"
string11 = "1234"
print(string8.isalpha())
#
print(string9.isalpha())
#
print(string10.isalnum())
#
print(string11.isdecimal())
#


wordlist = ["Toy Story", "Andy", "Buzz Lightyear", "Mr. Toad", "Mr. Tumbler"]
separator = ", "
print(separator.join(wordlist))

